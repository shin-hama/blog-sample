# Calendar API Demo Project

This is demonstration for google calendar api

## how to use

1. Create GCP Project and enable api for google calender
2. Create OAuth settings or service accounts.
3. Save credentials information as`credentials_client.json` or `credentials_service.json` from Google Cloud Platform
    - `credentials_client.json`: OAuth client key
    - `credentials_service.json`: Service Account key
4. Install dependency

    ```shell
    # if you use poetry
    poetry install

    # else
    pip install -r requirements.txt
    ```

5. Run script.
6. You can get events from your calender.
