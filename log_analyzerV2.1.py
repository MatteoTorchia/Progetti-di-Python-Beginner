import re
from collections import Counter

# Simula il contenuto del file 'events.log'
# (In un secondo momento, potrai sostituire questo con la lettura di un file reale)

log_data_content = """
INFO: Server startup complete
WARNING: Low disk space
ERROR: Database connection failed
INFO: User 'admin' logged in
DEBUG: Checking user permissions
INFO: Data processed successfully
ERROR: File not found 'config.ini'
WARNING: API timeout detected
INFO: User 'guest' logged in
DEBUG: Variable 'x' = 10
INFO: Server shutdown initiated
"""

def data_extractor(log_content):
    pattern = r"(INFO: User '(?P<username>.+?)' logged in)|(ERROR: File not found '(?P<filename>.+?)')"
    matches = re.finditer(pattern, log_content)

    extracted_data = []
    for match in matches:
        match_dict = match.groupdict()        
        extracted_data.append(match_dict)

    return [d for d in extracted_data if any(d.values())]


def log_analyzer_regex(log_content):
    events = {}  #dictionary with event_type and how many times the event appeared

    events = re.findall("^([A-Z]+):", log_content, re.MULTILINE)
    count_events = Counter(events)

    return count_events


def print_report(events):
    print("\nReport Frequenza Eventi:")
    print("------------------------------------------------")
    for event_type, count in events.items():
        print(f"Evento: {event_type:<10} -> Conteggio: {count}")
    print("------------------------------------------------")



# --- Flusso Principale ---
extracted_info = data_extractor(log_data_content)
print("\nDati Estratti:")
print("------------------------------------------------")
for item in extracted_info:
    print(item)


log_simulato = log_data_content

events = log_analyzer_regex(log_simulato)
print_report(events)