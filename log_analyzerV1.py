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

def log_analyzer(log_content):
    events = {}  #dictionary with event_type and how many times the event appeared

    log_content_splitted = log_content.splitlines()
    for line in log_content_splitted:
        if line:
            cleaned_line = line.strip()
            line_words = cleaned_line.split()
            first_word = line_words[0]  
            cleaned_first_word = event_type = first_word.strip(":")
            
            if event_type in events:
                events[event_type] += 1
            else:
                events[event_type] = 1
    
    return events


def print_report(events):
    print("Report Frequenza Eventi:")
    print("------------------------")
    for event_type, count in events.items():
        print(f"Evento: {event_type:<10} -> Conteggio: {count}")
    print("------------------------")



# --- Flusso Principale ---
log_simulato = log_data_content 
# (Più tardi qui useremo 'with open...')

events = log_analyzer(log_simulato)
print_report(events)