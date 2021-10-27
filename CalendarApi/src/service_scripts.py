from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google.auth import load_credentials_from_file

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # Load credential file for service account
    creds = load_credentials_from_file(
      'credentials_service.json', SCOPES
    )[0]


    # Calender API を利用するクライアントを生成
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    # NOTE: Set your calendar id
    events_result = service.events().list(calendarId='YourCalendarID@google.com', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()
