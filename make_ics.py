from ics import Calendar, Event


def make_ics(ophaaldata):
    cal = Calendar()
    for data in ophaaldata:
        event = Event()
        event.name = data['title']
        event.begin = data['ophaaldatum']
        event.make_all_day()
        event.description = data['content']
        event.url = data['link']
        cal.events.add(event)
    cal_bytes = bytes(str(cal), 'utf-8')
    return cal_bytes
