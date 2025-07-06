"""Task 1 Request Queue Simulation solution"""

from queue import Queue
import random
import logging
import time

from request import Request

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s"
)


def generate_request(request_queue: Queue) -> None:
    """Generates a new request and adds it to the queue."""
    new_request = Request(
        {
            # Some request payload with managed_by, client_id, issue_type, issue_desc, etc. info
            # Simulate real data
            "managed_by": random.choice(["Alice", "Bob", "Charlie"]),
            "client_id": random.randint(1000, 9999),
            "issue_type": random.choice(["Network", "Software", "Hardware"]),
            "issue_desc": "Auto-generated issue report.",
        }
    )
    request_queue.put(new_request)
    logging.info(
        "➕ Added new request with following request ID: %s", repr(new_request)
    )


def process_request(request_queue: Queue) -> None:
    """Processes the next request from the queue."""
    if not request_queue.empty():
        request = request_queue.get()
        logging.info("⚙️ Processing request: %s", repr(request))
        time.sleep(random.uniform(0.5, 2.0))  # Simulate variable processing delay
        logging.info("✔️ Processed request: %s", repr(request))
    else:
        logging.info("⚪ Queue is empty. No requests to process.")


def main() -> None:
    """
    Main loop to simulate continuous request generation and processing.
    """
    # Create a request queue
    request_queue: Queue = Queue()

    print("🔁 Application started. Press Ctrl+C to quit.\n")

    try:
        while True:
            if random.choice([True, False]):
                # Generate request
                generate_request(request_queue)

            if random.choice([True, False]):
                # Process request
                process_request(request_queue)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")


if __name__ == "__main__":
    main()
