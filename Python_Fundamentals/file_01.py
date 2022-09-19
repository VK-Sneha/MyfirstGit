def studies(amount_paid):

    if amount_paid == "10K":
        print("Medical materials are available for this price")

    if amount_paid == "2K":
        print("Engineering materials are avaiable for this price but not materials of Medical")

studies("10K")
studies("2K")
