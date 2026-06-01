import random
from datetime import datetime, timedelta

from services.data_repository import load_json_data, save_json_data
from services.report_manager import build_status_summary, generate_report_charts
from services.table_formatter import print_records_table, print_single_record_table
from services.telemetry_processor import process_raw_telemetry, search_processed_record


INPUT_PATH = "data/agrosphere_telemetry.json"
OUTPUT_PATH = "data/analyzed_telemetry.json"
DEFAULT_RANDOM_RECORDS = 30
DEFAULT_DISPLAY_LIMIT = 10


def show_welcome():
    print()
    print("=" * 56)
    print("Oi, bem-vindo ao AgroSphere!")
    print("Sistema de telemetria para suporte agrícola em ambientes extremos.")
    print("=" * 56)


def show_menu():
    print()
    print("-" * 56)
    print("MENU PRINCIPAL")
    print("-" * 56)
    print("1 - Processar dados")
    print("2 - Consultar dados processados")
    print("3 - Ver dados não processados")
    print("4 - Gerar nova base de dados aleatórios")
    print("5 - Buscar dado processado por ID")
    print("6 - Limpar dados processados")
    print("7 - Ver resumo e gerar gráficos")
    print("0 - Sair")
    print("-" * 56)


def show_processed_data_menu():
    print()
    print("-" * 56)
    print("CONSULTA DE DADOS PROCESSADOS")
    print("-" * 56)
    print("1 - Ver todos")
    print("2 - Ver dados críticos")
    print("3 - Ver dados em alerta")
    print("4 - Ver dados estáveis")
    print("0 - Voltar")
    print("-" * 56)


def ask_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Digite um número inteiro válido.")


def ask_positive_int(message):
    while True:
        value = ask_int(message)

        if value > 0:
            return value

        print("Digite um número maior que zero.")


def ask_minimum_int(message, minimum):
    while True:
        value = ask_positive_int(message)

        if value >= minimum:
            return value

        print(f"Digite um número maior ou igual a {minimum}.")


def generate_random_timestamp(index):
    start = datetime(2026, 5, 27, 8, 0, 0)
    timestamp = start + timedelta(minutes=index * 5)
    return timestamp.strftime("%Y-%m-%dT%H:%M:%S")


def build_random_telemetry_record(record_id):
    modules = [
        "Módulo-Hidropônico-A",
        "Módulo-Hidropônico-B",
        "Módulo-Biorreator-C",
        "Módulo-Reciclagem-D",
    ]
    module_name = random.choice(modules)
    sector_number = random.randint(1, 10)

    return {
        "id": record_id,
        "timestamp": generate_random_timestamp(record_id - 1),
        "sector": f"{module_name}{sector_number:02d}",
        "oxygen_percent": round(random.uniform(17.5, 21.0), 1),
        "co2_ppm": random.randint(750, 1650),
        "temperature_celsius": round(random.uniform(18.0, 32.0), 1),
        "humidity_percent": random.randint(42, 86),
        "water_reserve_liters": random.randint(230, 540),
        "solar_energy_kw": round(random.uniform(3.6, 7.0), 1),
        "plant_health_percent": random.randint(48, 97),
    }


def build_random_database(quantity):
    records = []

    for record_id in range(1, quantity + 1):
        records.append(build_random_telemetry_record(record_id))

    return records


def generate_new_random_database():
    quantity = ask_minimum_int(
        f"Quantos registros deseja gerar? Mínimo obrigatório: {DEFAULT_RANDOM_RECORDS}: ",
        DEFAULT_RANDOM_RECORDS,
    )

    records = build_random_database(quantity)
    save_json_data(records, INPUT_PATH)
    save_json_data([], OUTPUT_PATH)

    print()
    print(f"Nova base não processada criada com {quantity} registros.")
    print("Os dados processados foram limpos para evitar mistura de bases.")


def process_data():
    raw_records = load_json_data(INPUT_PATH)

    if len(raw_records) == 0:
        print()
        print("Nenhum dado não processado ainda.")
        return

    print()
    print(f"Existem {len(raw_records)} dados não processados na fila.")
    quantity = ask_positive_int("Quantos registros deseja processar agora? ")

    try:
        result = process_raw_telemetry(INPUT_PATH, OUTPUT_PATH, quantity)
    except ValueError as error:
        print()
        print(f"Erro: {error}")
        return

    summary = result["summary"]

    print()
    print("-" * 56)
    print("Processamento concluído!")
    print(f"Registros que estavam na fila: {result['loaded']}")
    print(f"Registros processados pela fila FIFO: {result['processed']}")
    print(f"Registros restantes na fila: {result['remaining']}")
    print(f"Estáveis: {summary['stable']}")
    print(f"Em alerta: {summary['warning']}")
    print(f"Críticos: {summary['critical']}")
    print("-" * 56)


def show_records(records, title):
    print()
    print("-" * 56)
    print(title)
    print(f"Total de registros: {len(records)}")
    print("-" * 56)

    if len(records) == 0:
        print("Nenhum dado ainda.")
        return

    print_records_table(records, DEFAULT_DISPLAY_LIMIT)


def show_raw_data():
    records = load_json_data(INPUT_PATH)
    show_records(records, "Dados não processados")


def load_processed_records():
    records = load_json_data(OUTPUT_PATH)

    if len(records) == 0:
        print()
        print("Nenhum dado processado ainda.")

    return records


def filter_records_by_status(records, status):
    filtered_records = []

    for record in records:
        if record.get("status") == status:
            filtered_records.append(record)

    return filtered_records


def show_processed_records_by_status(status, title):
    records = load_processed_records()

    if len(records) == 0:
        return

    filtered_records = filter_records_by_status(records, status)
    show_records(filtered_records, title)


def show_all_processed_data():
    records = load_processed_records()

    if len(records) == 0:
        return

    show_records(records, "Todos os dados processados")


def handle_processed_data_option(option):
    if option == "1":
        show_all_processed_data()
    elif option == "2":
        show_processed_records_by_status("CRITICAL", "Dados que apresentam risco crítico")
    elif option == "3":
        show_processed_records_by_status("WARNING", "Dados em alerta")
    elif option == "4":
        show_processed_records_by_status("STABLE", "Dados estáveis")
    elif option == "0":
        return False
    else:
        print("Opção inválida.")

    return True


def show_processed_data_controller():
    keep_running = True

    while keep_running:
        show_processed_data_menu()
        option = input("Escolha uma opção: ").strip()
        keep_running = handle_processed_data_option(option)


def search_processed_data():
    processed_records = load_json_data(OUTPUT_PATH)

    if len(processed_records) == 0:
        print()
        print("Nenhum dado processado ainda.")
        return

    target_id = ask_int("Digite o ID para buscar: ")
    found_record = search_processed_record(OUTPUT_PATH, target_id)

    print()

    if found_record is None:
        print("Registro processado não encontrado.")
        return

    print("Registro encontrado pela busca binária recursiva:")
    print_single_record_table(found_record)


def clear_processed_data():
    processed_records = load_json_data(OUTPUT_PATH)

    if len(processed_records) == 0:
        print()
        print("Nenhum dado processado ainda.")
        return

    save_json_data([], OUTPUT_PATH)

    print()
    print("Dados processados limpos com sucesso.")


def show_summary_and_charts():
    records = load_json_data(OUTPUT_PATH)

    if len(records) == 0:
        print()
        print("Nenhum dado processado ainda.")
        return

    summary = build_status_summary(records)
    chart_paths = generate_report_charts(records)

    print()
    print("-" * 56)
    print("RESUMO OPERACIONAL")
    print("-" * 56)
    print(f"Total processado: {summary['total_processados']}")
    print(f"Estáveis: {summary['estaveis']}")
    print(f"Em alerta: {summary['em_alerta']}")
    print(f"Críticos / urgentes: {summary['criticos']}")
    print(f"Total de alertas detectados: {summary['total_alertas']}")
    print("-" * 56)

    if not chart_paths["matplotlib_available"]:
        print("Matplotlib não está instalado neste ambiente.")
        print("Para gerar os gráficos, execute: python -m pip install -r requirements.txt")
        return

    if chart_paths["status_chart"] is not None:
        print(f"Gráfico de status salvo em: {chart_paths['status_chart']}")

    if chart_paths["alerts_chart"] is not None:
        print(f"Gráfico de alertas salvo em: {chart_paths['alerts_chart']}")
    else:
        print("Nenhum alerta encontrado para gerar gráfico de alertas.")


def handle_option(option):
    if option == "1":
        process_data()
    elif option == "2":
        show_processed_data_controller()
    elif option == "3":
        show_raw_data()
    elif option == "4":
        generate_new_random_database()
    elif option == "5":
        search_processed_data()
    elif option == "6":
        clear_processed_data()
    elif option == "7":
        show_summary_and_charts()
    elif option == "0":
        print("Encerrando o AgroSphere. Até logo!")
        return False
    else:
        print("Opção inválida.")

    return True


def start_application():
    show_welcome()

    keep_running = True

    while keep_running:
        show_menu()
        option = input("Escolha uma opção: ").strip()
        keep_running = handle_option(option)
