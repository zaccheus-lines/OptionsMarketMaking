import blpapi

def main():
    # Create and start a session
    session = blpapi.Session()
    if not session.start():
        print("Failed to start session.")
        return

    if not session.openService("//blp/refdata"):
        print("Failed to open //blp/refdata")
        return

    refDataService = session.getService("//blp/refdata")
    request = refDataService.createRequest("ReferenceDataRequest")

    # Replace these with actual option identifiers
    securities = [
        "AAPL 12/15/23 C185 Equity", "AAPL 12/15/23 C185 Equity"
    ]


    fields = [
        "OPT_STRIKE_PX", "DAYS_TO_EXPIRY",
        "BID", "BID_SIZE", "ASK", "ASK_SIZE",
        "BID_PX", "BID_SIZE", "ASK_PX", "ASK_SIZE"
    ]

    for security in securities:
        request.append("securities", security)

    for field in fields:
        request.append("fields", field)

    # Send the request
    print("Sending Request:", request)
    session.sendRequest(request)

    # Process received events
    while True:
        ev = session.nextEvent()
        for msg in ev:
            if ev.eventType() == blpapi.Event.RESPONSE:
                print("Response received:", msg)
                # Process the response message to extract data

        if ev.eventType() == blpapi.Event.RESPONSE:
            # End of the response
            break

    session.stop()

if __name__ == "__main__":
    main()