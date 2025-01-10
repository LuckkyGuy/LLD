from entity import Auction, Seller, Buyer


class AuctionSystem:
    def __init__(self):
        self.buyers = dict()
        self.sellers = dict()
        self.auctions = dict()

    def add_buyer(self, name):
        if name in self.buyers:
            raise ValueError("Buyer already exists.")
        self.buyers[name] = Buyer(name)

    def add_seller(self, name):
        if name in self.sellers:
            raise ValueError("Seller already exists.")
        self.sellers[name] = Seller(name)

    def create_auction(self, auction_id, lowest_bid_limit, highest_bid_limit, participation_cost, seller_name):
        if auction_id in self.auctions:
            raise ValueError("Auction already exists.")
        if seller_name not in self.sellers:
            raise ValueError("Seller does not exist.")

        seller = self.sellers[seller_name]
        auction = Auction(auction_id, lowest_bid_limit, highest_bid_limit, participation_cost, seller)
        self.auctions[auction_id] = auction

    def create_or_update_bid(self, buyer_name, auction_id, amount):
        if buyer_name not in self.buyers:
            raise ValueError("Buyer does not exist.")
        if auction_id not in self.auctions:
            raise ValueError("Auction does not exist.")

        buyer = self.buyers[buyer_name]
        auction = self.auctions[auction_id]
        auction.create_or_update_bid(buyer_name, amount)

    def withdraw_bid(self, buyer_name, auction_id):
        if buyer_name not in self.buyers:
            raise ValueError("Buyer does not exist.")
        if auction_id not in self.auctions:
            raise ValueError("Auction does not exist.")

        buyer = self.buyers[buyer_name]
        auction = self.auctions[auction_id]
        auction.withdraw_bid(buyer_name)

    def close_auction(self, auction_id):
        if auction_id not in self.auctions:
            raise ValueError("Auction does not exist.")

        auction = self.auctions[auction_id]
        return auction.close()

    def get_profit_or_loss(self, seller_name, auction_id):
        if seller_name not in self.sellers:
            raise ValueError("Seller does not exist.")
        if auction_id not in self.auctions:
            raise ValueError("Auction does not exist.")

        auction = self.auctions[auction_id]
        return auction.calculate_profit_or_loss()