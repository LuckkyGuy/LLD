class User:
    def __init__(self, name):
        self.name = name
        self.participated_auctions = set()

    def add_auction(self, auction_id):
        self.participated_auctions.add(auction_id)

    
class Seller(User):
    def __init__(self, name):
        super().__init__(name)

class Buyer(User):
    def __init__(self, name):
        super().__init__(name)

    def is_preferred(self):
        return len(self.participated_auctions) > 2


class Auction:
    def __init__(self, auction_id, lowest_bid_limit, highest_bid_limit, participation_cost, seller):
        self.auction_id = auction_id
        self.lowest_bid_limit = lowest_bid_limit
        self.highest_bid_limit = highest_bid_limit
        self.participation_cost = participation_cost
        self.seller = seller
        self.bids = {}
        self.participants = 0
        self.closed = False

    def create_or_update_bid(self, buyer, amount):
        if self.closed:
            raise ValueError("Auction is already closed.")
        if amount < self.lowest_bid_limit or amount > self.highest_bid_limit:
            print("This is not valid bid")
            return
            # raise ValueError("Bid is out of allowed range.")
        self.bids[buyer] = amount
        self.participants = max(self.participants, len(self.bids))
        self.bids[buyer].add_auction(self.auction_id)

    def withdraw_bid(self, buyer):
        if self.closed:
            raise ValueError("Auction is already closed.")
        if buyer in self.bids:
            del self.bids[buyer]

    def close(self):
        if self.closed:
            raise ValueError("Auction is already closed.")
        return self._close()
        
    
    def _close(self):
        self.closed = True
        bid_counts = {}
        for amount in self.bids.values():
            bid_counts[amount] = bid_counts.get(amount, 0) + 1

        unique_bids = [amount for amount, count in bid_counts.items() if count == 1]
        # if unique_bids:
        #     highest_unique_bid = max(unique_bids)
        #     winners = [buyer for buyer, amount in self.bids.items() if amount == highest_unique_bid]
        #     # preferred_winners = [buyer for buyer in winners if buyer.is_preferred()]

        #     # if preferred_winners:
        #     #     return preferred_winners[0]
        #     return winners[0]

        bider_data = sorted(self.bids.items(), key = lambda x: (-x[1], x[0].is_preferred()))
        winner, amount, preffered = None, -1, False
        for i in range(len(bider_data)):
            if bider_data[i][1] == amount:
                if preffered == bider_data[i][0].is_preferred():
                    winner, amount, preffered = None, -1, False
                else:
                    pass
            else:
                winner, amount, preffered = bider_data[i][0], bider_data[i][1], bider_data[0].is_preferred()
        return winner


    def calculate_profit_or_loss(self):
        # no_of_bidders = len(self.bids)
        participation_share = self.participants * 0.2 * self.participation_cost
        average_limit = (self.lowest_bid_limit + self.highest_bid_limit) / 2
        
        winning_bid = self._close()
        if winning_bid:
            return self.bids[winning_bid] + participation_share - average_limit
        return participation_share
    