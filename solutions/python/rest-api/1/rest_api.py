import json
class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        main_key = [item for item in self.database.keys() if item in url]

        if len(main_key)==0:
            return []

        main_key = main_key[0]

        if not payload:
            return json.dumps(self.database)

        payload = json.loads(payload)
        out=[item for item in self.database["users"] if item["name"] in payload["users"]]

        return json.dumps({"users":out})

    def post(self, url, payload=None):
        if url == "/add":
            base = {"name": "",
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0}
            if payload:
                payload = json.loads(payload)
                for key in payload.keys():
                    key_2 = key
                    if key == "user":
                        key_2  = "name"
                        
                    base[key_2] = payload[key]
            if base["name"] not in [item["name"] for item in self.database["users"]]:
                self.database["users"].append(base)
                return json.dumps(base)     
        elif url == "/iou":
            payload = json.loads(payload)

            lender = payload["lender"]
            borrower = payload["borrower"]
            amount = payload["amount"]

            self.post("/add",json.dumps({"user": lender}))
            self.post("/add",json.dumps({"user": borrower}))

            idx_lender = [pos for pos in range(len(self.database["users"])) if self.database["users"][pos]["name"] == lender][0]
            idx_borrower = [pos for pos in range(len(self.database["users"])) if self.database["users"][pos]["name"] == borrower][0]

            #owes prestar a
            #owned quien me presto
            
            #define values lender
            lender_owned = self.database["users"][idx_lender]["owed_by"]
            lender_owes = self.database["users"][idx_lender]["owes"]

            if borrower in lender_owes.keys():
                self.database["users"][idx_lender]["owes"][borrower] -= amount
                
                value = self.database["users"][idx_lender]["owes"][borrower]
                if value == 0:
                    del self.database["users"][idx_lender]["owes"][borrower]
                elif value < 0:
                    self.database["users"][idx_lender]["owed_by"].update({borrower:abs(value)})
                    del self.database["users"][idx_lender]["owes"][borrower]
                    
            elif borrower in lender_owned.keys():
                self.database["users"][idx_lender]["owed_by"][borrower] -= amount
                value = self.database["users"][idx_lender]["owed_by"][borrower]
                if value == 0:
                    del self.database["users"][idx_lender]["owed_by"][borrower]
                elif value < 0:
                    self.database["users"][idx_lender]["owes"].update({borrower:abs(value)})
                    del self.database["users"][idx_lender]["owed_by"][borrower]
            else:
                self.database["users"][idx_lender]["owed_by"].update({borrower:amount})
                
            

            #define values borrowe
            borrower_owned = self.database["users"][idx_borrower]["owed_by"]
            borrower_owes = self.database["users"][idx_borrower]["owes"]

            if lender in borrower_owes.keys():
                self.database["users"][idx_borrower]["owes"][lender] -= amount
                value = self.database["users"][idx_borrower]["owed_by"][lender]
                if value == 0:
                    del self.database["users"][idx_borrower]["owed_by"][lender]
                elif value < 0:
                    self.database["users"][idx_borrower]["owes"].update({lender:abs(value)})
                    del self.database["users"][idx_borrower]["owed_by"][lender]
            elif lender in borrower_owned.keys():
                self.database["users"][idx_borrower]["owed_by"][lender] -= amount

                value = self.database["users"][idx_borrower]["owed_by"][lender]
                if value == 0:
                    del self.database["users"][idx_borrower]["owed_by"][lender]
                elif value < 0:
                    self.database["users"][idx_borrower]["owes"].update({lender:abs(value)})
                    del self.database["users"][idx_borrower]["owed_by"][lender]
                    
            else:
                self.database["users"][idx_borrower]["owes"].update({lender:amount})
            
            
            #deifne new balance
            self.database["users"][idx_lender]["balance"] += amount
            self.database["users"][idx_borrower]["balance"] -= amount

            data_1 = self.get("/users",json.dumps({"users": [lender,borrower]}))

            print(self.database["users"][idx_lender])
            print(self.database["users"][idx_borrower])
            print("- - - -")
            print(data_1)
            return data_1
            
