# https://docs.google.com/document/d/1ll53poCgwqDBkpi4880dRtBD8EjGhGvoXc98INFt0sA/edit?tab=t.0

from AuctionSystem import AuctionSystem

# Example Usage
def main():
    system = AuctionSystem()

    # Test Case 1
    system.add_buyer("buyer1")
    system.add_buyer("buyer2")
    system.add_buyer("buyer3")
    system.add_seller("seller1")
    system.create_auction("A1", 10, 50, 1, "seller1")

    system.create_or_update_bid("buyer1", "A1", 17)
    system.create_or_update_bid("buyer2", "A1", 15)
    system.create_or_update_bid("buyer2", "A1", 19)  # Updated bid
    system.create_or_update_bid("buyer3", "A1", 19)

    winner = system.close_auction("A1")
    print("Winner:", winner.name if winner else "No winner")

    profit_or_loss = system.get_profit_or_loss("seller1", "A1")
    print("Profit/Loss:", profit_or_loss)


    # Test Case 2
    system.add_seller("seller2")
    system.create_auction("A2", 5, 20, 2, "seller2")   
    system.create_or_update_bid("buyer3", "A2", 25)  
    system.create_or_update_bid("buyer2", "A2", 5)  
    system.withdraw_bid("buyer2", "A2") 
    winner = system.close_auction("A2")
    profit_or_loss = system.get_profit_or_loss("seller2", "A2")
    print("Profit/Loss:", profit_or_loss)

if __name__ == "__main__":
    main()