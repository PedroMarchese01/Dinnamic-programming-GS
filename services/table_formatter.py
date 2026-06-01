import pandas as pd


DISPLAY_COLUMNS = {
    "id": "ID",
    "timestamp": "Horário",
    "sector": "Setor",
    "oxygen_percent": "O2 (%)",
    "co2_ppm": "CO2 (ppm)",
    "temperature_celsius": "Temp (°C)",
    "humidity_percent": "Umidade (%)",
    "water_reserve_liters": "Água (L)",
    "solar_energy_kw": "Energia (kW)",
    "plant_health_percent": "Saúde (%)",
    "status": "Status",
    "risk_score": "Risco",
    "alerts": "Alertas",
}

STATUS_LABELS = {
    "CRITICAL": "CRÍTICO",
    "WARNING": "EM ALERTA",
    "STABLE": "ESTÁVEL",
}

ALERT_LABELS = {
    "LOW_OXYGEN": "oxigênio baixo",
    "HIGH_CO2": "CO2 elevado",
    "LOW_WATER_RESERVE": "reserva de água baixa",
    "UNSAFE_TEMPERATURE": "temperatura fora do ideal",
    "UNSAFE_HUMIDITY": "umidade fora do ideal",
    "LOW_PLANT_HEALTH": "saúde das plantas baixa",
    "LOW_SOLAR_ENERGY": "energia solar baixa",
}


def normalize_alerts(alerts):
    if not isinstance(alerts, list) or len(alerts) == 0:
        return "nenhum"

    alert_labels = [ALERT_LABELS.get(alert, alert) for alert in alerts]
    return ", ".join(alert_labels)


def normalize_status(status):
    return STATUS_LABELS.get(status, status)


def build_records_dataframe(records):
    dataframe = pd.DataFrame(records)

    if dataframe.empty:
        return dataframe

    if "alerts" in dataframe.columns:
        dataframe["alerts"] = dataframe["alerts"].apply(normalize_alerts)

    if "status" in dataframe.columns:
        dataframe["status"] = dataframe["status"].apply(normalize_status)

    available_columns = []

    for column in DISPLAY_COLUMNS:
        if column in dataframe.columns:
            available_columns.append(column)

    dataframe = dataframe[available_columns]
    dataframe = dataframe.rename(columns=DISPLAY_COLUMNS)

    return dataframe


def print_records_table(records, limit):
    dataframe = build_records_dataframe(records)

    if dataframe.empty:
        print("Nenhum dado ainda.")
        return

    preview = dataframe.head(limit)
    print(preview.to_string(index=False))

    hidden_records = len(dataframe) - len(preview)

    if hidden_records > 0:
        print(f"... mais {hidden_records} registros não exibidos.")
        print(f"A interface mostra uma prévia de {limit} registros por consulta.")


def print_single_record_table(record):
    print_records_table([record], 1)
