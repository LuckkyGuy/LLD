# https://leetcode.com/discuss/interview-question/4491846/Wayfair-or-SDE2-L2-4-Onsite-Virtual-or-Coupon-category
# https://leetcode.com/discuss/interview-question/4799068/Wayfair-or-Onsite-or-Round-1-DSA-or-Bangalore

from collections import defaultdict
from datetime import datetime

Coupons = [
    { "CategoryName": "Comforter Sets", "CouponName": "Comforters Sale", "DateModified":"2020-01-01"},
    { "CategoryName":"Comforter Sets", "CouponName": "Cozy Comforter Coupon", "DateModified": "2020-01-01" }, 
    { "CategoryName":"Bedding", "CouponName": "Best Bedding Bargains", "DateModified": "2019-01-01" },
    { "CategoryName":"Bedding", "CouponName": "Savings on Bedding", "DateModified": "2019-01-01"},
    { "CategoryName":"Bed & Bath", "CouponName": "Low price for Bed & Bath", "DateModified": "2018-01-01" },
    { "CategoryName":"Bed & Bath", "CouponName":"Bed & Bath extravaganza", "DateModified":"2019-01-01" },
    { "CategoryName":"Bed & Bath", "CouponName":"Big Savings for Bed & Bath", "DateModified":"2030-01-01" }
]

Categories = [
    {"CategoryName":"Comforter Sets", "Category ParentName":"Bedding"},
    {"CategoryName":"Bedding", "CategoryParentName": "Bed & Bath"},
    {"CategoryName":"Bed & Bath", "CategoryParentName": None},
    {"CategoryName":"Soap Dispensers", "Category ParentName": "Bathroom Accessories"}, 
    {"CategoryName":"Bathroom Accessories", "CategoryParentName": "Bed & Bath"},
    {"CategoryName":"Toy Organizers", "CategoryParentName": "Baby And"}
]

CATAGORY_NAME = "CategoryName"
COUPON_NAME = "CouponName"
CATAGORY_PARENT_NAME = "CategoryParentName"
DATE_MODIFIED = "DateModified"

class Coupon:
    def __init__(self, name, modifiedDate):
        self.name = name
        self.lastModifiedDate = modifiedDate
    
class Solution:
    def __init__(self, categories, coupons):
        self.coupons = defaultdict(lambda : None)
        self.adj = defaultdict(list)
        self.root = []
        self.vis = defaultdict(int)
        self.initialize(categories, coupons)

    # fetch the Data from DataSet.
    def initialize(self, categories, coupons):
        for coupon in coupons:
            category_name = coupon.get(CATAGORY_NAME)
            coupon_name = coupon.get(COUPON_NAME)
            datetime_str = coupon.get(DATE_MODIFIED)
            modifiedDate = datetime.strptime(datetime_str, '%Y-%m-%d')
            if not self.coupons[category_name] or \
            self.coupons[category_name].lastModifiedDate <= modifiedDate <= datetime.today():
                self.coupons[category_name] = Coupon(coupon_name, modifiedDate) 

        for categorie in categories:
            category_name = categorie.get(CATAGORY_NAME)
            category_parent_name = categorie.get(CATAGORY_PARENT_NAME)
            if category_parent_name == None:
                self.root.append(category_name)
            else: 
                self.adj[category_parent_name].append(category_name)
        
        for node in self.root:
            self.dfs(node, None)

    # If given category don't have coupon then fetch the coupon from the parent category.
    def dfs(self, curr, parent):
        self.vis[curr] = 1
        if not self.coupons[curr] and parent:
            self.coupons[curr] = self.coupons[parent]    
        for child in self.adj[curr]:
            if not self.vis[child]:
                self.dfs(child, curr)
    
    # perform the query in O(1) time
    def find_query(self, category_name):
        if self.coupons[category_name]:
            return self.coupons[category_name].name
        return "None"

solution = Solution(Categories, Coupons)
ans = solution.find_query("Bed & Bath")
print(ans)


from sortedcontainers import SortedList
s = SortedList()
s.add(1)
s.add(2)

print(s)
