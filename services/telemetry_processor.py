from services.data_repository import load_json_data, save_json_data
from services.queue_manager import create_queue, dequeue, is_queue_empty, queue_size
from services.recursive_binary_search import (
    recursive_binary_search_by_id,
    sort_records_by_id,
)
from services.telemetry_analyzer import analyze_telemetry_record, summarize_analysis


MINIMUM_REQUIRED_RECORDS = 30


def validate_dataset(records, minimum_required=1):
    if len(records) < minimum_required:
        raise ValueError(
            f"A base precisa ter pelo menos {minimum_required} registro(s) para processar."
        )


def process_telemetry_queue(records, quantity):
    telemetry_queue = create_queue(records)
    analyzed_records = []

    while not is_queue_empty(telemetry_queue) and len(analyzed_records) < quantity:
        telemetry_record = dequeue(telemetry_queue)
        analyzed_record = analyze_telemetry_record(telemetry_record)
        analyzed_records.append(analyzed_record)

    remaining_records = []

    while not is_queue_empty(telemetry_queue):
        remaining_records.append(dequeue(telemetry_queue))

    return analyzed_records, remaining_records


def process_raw_telemetry(input_path, output_path, quantity):
    records = load_json_data(input_path)
    validate_dataset(records)

    quantity_to_process = min(quantity, len(records))
    processed_records, remaining_records = process_telemetry_queue(
        records,
        quantity_to_process,
    )
    previously_processed_records = load_json_data(output_path)
    updated_processed_records = previously_processed_records + processed_records

    save_json_data(remaining_records, input_path)
    save_json_data(updated_processed_records, output_path)

    return {
        "loaded": len(records),
        "processed": len(processed_records),
        "remaining": len(remaining_records),
        "summary": summarize_analysis(processed_records),
    }


def search_processed_record(output_path, target_id):
    processed_records = load_json_data(output_path)
    sorted_records = sort_records_by_id(processed_records)
    return recursive_binary_search_by_id(sorted_records, target_id)
