def identify_alerts(record):
    alerts = []

    if record["oxygen_percent"] < 19.5:
        alerts.append("LOW_OXYGEN")

    if record["co2_ppm"] > 1200:
        alerts.append("HIGH_CO2")

    if record["water_reserve_liters"] < 320:
        alerts.append("LOW_WATER_RESERVE")

    if record["temperature_celsius"] < 18 or record["temperature_celsius"] > 28:
        alerts.append("UNSAFE_TEMPERATURE")

    if record["humidity_percent"] < 45 or record["humidity_percent"] > 75:
        alerts.append("UNSAFE_HUMIDITY")

    if record["plant_health_percent"] < 70:
        alerts.append("LOW_PLANT_HEALTH")

    if record["solar_energy_kw"] < 4.5:
        alerts.append("LOW_SOLAR_ENERGY")

    return alerts


def calculate_risk_score(record, alerts):
    score = len(alerts) * 15

    if record["plant_health_percent"] < 60:
        score += 20

    if record["water_reserve_liters"] < 260:
        score += 20

    if record["oxygen_percent"] < 18.5:
        score += 25

    return min(score, 100)


def classify_status(risk_score):
    if risk_score >= 60:
        return "CRITICAL"

    if risk_score >= 25:
        return "WARNING"

    return "STABLE"


def analyze_telemetry_record(record):
    analyzed_record = record.copy()
    alerts = identify_alerts(analyzed_record)
    risk_score = calculate_risk_score(analyzed_record, alerts)

    analyzed_record["alerts"] = alerts
    analyzed_record["risk_score"] = risk_score
    analyzed_record["status"] = classify_status(risk_score)

    return analyzed_record


def summarize_analysis(records):
    summary = {
        "stable": 0,
        "warning": 0,
        "critical": 0,
    }

    for record in records:
        status = record["status"].lower()
        summary[status] += 1

    return summary
 