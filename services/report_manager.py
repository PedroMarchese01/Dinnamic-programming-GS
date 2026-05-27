from pathlib import Path

import pandas as pd


try:
    import matplotlib
    import matplotlib.pyplot as plt

    matplotlib.use("Agg")
except ImportError:
    matplotlib = None
    plt = None

REPORTS_PATH = Path("reports")

STATUS_LABELS = {
    "CRITICAL": "Criticos",
    "WARNING": "Em alerta",
    "STABLE": "Estaveis",
}


def build_processed_dataframe(records):
    dataframe = pd.DataFrame(records)

    if dataframe.empty:
        return dataframe

    if "status" in dataframe.columns:
        dataframe["status_label"] = dataframe["status"].map(STATUS_LABELS)

    return dataframe


def count_alert_occurrences(records):
    alert_counts = {}

    for record in records:
        for alert in record.get("alerts", []):
            if alert not in alert_counts:
                alert_counts[alert] = 0

            alert_counts[alert] += 1

    return alert_counts


def build_status_summary(records):
    dataframe = build_processed_dataframe(records)

    summary = {
        "total_processados": len(records),
        "estaveis": 0,
        "em_alerta": 0,
        "criticos": 0,
        "total_alertas": 0,
    }

    if dataframe.empty:
        return summary

    status_counts = dataframe["status"].value_counts().to_dict()
    alert_counts = count_alert_occurrences(records)

    summary["estaveis"] = status_counts.get("STABLE", 0)
    summary["em_alerta"] = status_counts.get("WARNING", 0)
    summary["criticos"] = status_counts.get("CRITICAL", 0)
    summary["total_alertas"] = sum(alert_counts.values())

    return summary


def ensure_reports_directory():
    REPORTS_PATH.mkdir(exist_ok=True)


def save_status_chart(records):
    if plt is None:
        return None

    ensure_reports_directory()
    dataframe = build_processed_dataframe(records)
    chart_path = REPORTS_PATH / "status_operacional.png"

    if dataframe.empty:
        return None

    counts = dataframe["status_label"].value_counts()

    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar", color=["#d1495b", "#edae49", "#4c956c"])
    plt.title("Resumo por Status Operacional")
    plt.xlabel("Status")
    plt.ylabel("Quantidade de registros")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return str(chart_path)


def save_alerts_chart(records):
    if plt is None:
        return None

    ensure_reports_directory()
    alert_counts = count_alert_occurrences(records)
    chart_path = REPORTS_PATH / "tipos_de_alerta.png"

    if len(alert_counts) == 0:
        return None

    dataframe = pd.DataFrame(
        list(alert_counts.items()),
        columns=["alerta", "quantidade"],
    ).sort_values("quantidade", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(dataframe["alerta"], dataframe["quantidade"], color="#2a9d8f")
    plt.title("Ocorrencias por Tipo de Alerta")
    plt.xlabel("Quantidade")
    plt.ylabel("Tipo de alerta")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return str(chart_path)


def generate_report_charts(records):
    if plt is None:
        return {
            "status_chart": None,
            "alerts_chart": None,
            "matplotlib_available": False,
        }

    return {
        "status_chart": save_status_chart(records),
        "alerts_chart": save_alerts_chart(records),
        "matplotlib_available": True,
    }
