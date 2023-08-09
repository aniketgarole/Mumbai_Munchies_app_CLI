import uuid


def addSnack(snack):
    with open("../data/snacks.txt", "r") as file:
        contents = file.read()
        if contents == "":
            list = []
        else:
            list = eval(contents)
        
        list.append(snack)
        
        with open("../data/snacks.txt", "w") as filew:
            filew.write(str(list))
            print("\n            Snack has been added to the inventory successfully!!\n")
            # print("\n           ********************************************\n")
        

    

def removeSnack(id):
    with open("../data/snacks.txt", "r") as filer:
        contents = filer.read() 
        if contents == "":
            list = []
            print("\n            Sorry, the inventory is empty")
            return False

        else:
            list = eval(contents)
            
            deleted_snack = [x for x in list if x["id"] == id]
            
            if (len(deleted_snack)):
                new_list = [x for x in list if x["id"] != id]

                with open("../data/snacks.txt", "w") as filew:
                    filew.write(str(new_list))
                    print("\n            Snack has been removed successfully!!\n")
                    return True

            else:
                print(f"\n            The snack with id {id} does not exist, please try different id")
                return False

    

def changeStatus(id):
    with open("../data/snacks.txt", "r") as filer:
        contents = filer.read() 
        if contents == "":
            list = []
            print("\n            Sorry, the inventory is empty")

        else:
            list = eval(contents)
            
            snack_to_update = [x for x in list if x["id"] == id] or []

            
            
            if (len(snack_to_update)):

                origional_snack = snack_to_update[0]
                
                enter_value = input(f"\n            The availibility status of id {id} is '{snack_to_update[0]['avail']}', if you want to change it '{'no' if snack_to_update[0]['avail'] == 'yes' else 'yes'}' please press enter")

                value = 'no' if snack_to_update[0]['avail'] == 'yes' else 'yes'

                snack_to_update[0]["avail"] = value


                updated_snack = snack_to_update[0]
                

                new_list = [x if x != origional_snack else updated_snack for x in list]

                with open("../data/snacks.txt", "w") as filew:
                    filew.write(str(new_list))
                    print("\n            Snack has been updated successfully!!\n")
                    return True

            else:
                print(f"\n            The snack with id '{id}' does not exist, please try different id\n")
                return False




def placeOrder(order):
    with open("../data/snacks.txt", "r") as filer:
        content = filer.read()
        
        if content == "":
            print("\n            Sorry, your order cannot be placed, inventory is out of stock")
            return False
        else:
            list = eval(content)
            snack_id = order['snack_id']
            snack = [x for x in list if x['id'] == snack_id] or []

            

            

            if len(snack):
                origional_snack = snack[0]
                quantity_in_inv = snack[0]['quantity']
                quantity_in_order = order['quantity']


                if (quantity_in_inv >= quantity_in_order):
                    updated_quantity = quantity_in_inv - quantity_in_order

                    total_cost = quantity_in_order * snack[0]['price']
                    
                    snack[0]['quantity'] = updated_quantity

                    if updated_quantity == 0:
                        snack[0]['avail'] = "no"

                    order["total_cost"] = total_cost

                    updated_snack = snack[0]

                    

                    with open("../data/orders.txt", "r") as orderfiler:
                        order_content = orderfiler.read()
                        if order_content == "":
                            order_list = []
                        else: 
                            order_list = eval(order_content)
                        
                        order_list.append(order)

                        with open("../data/orders.txt", "w") as orderfilew:
                            orderfilew.write(str(order_list))

                            with open("../data/snacks.txt", "w") as snackfilew:
                                updated_list_snacks = [x if x != origional_snack else updated_snack for x in list]

                                snackfilew.write(str(updated_list_snacks))
                                print("\n            Order placed successfully!!")
                                print(f"\n            The total cost of your order is {total_cost} RS. !!")
                                print("\n            Thank you for your patience, you will receive your order soon!!")
                            return True


                else:
                    print(f"\n            Sorry we don't have {quantity_in_order} items available right now, please change your order!!")
                    return False
                
            
            else:
                print(f"\n            Sorry, we don't have snack with id {snack_id} in our inventory, please try another snack!!")
                return False





def viewInventory():
    with open("../data/snacks.txt", "r") as filer:
        contents = filer.read()
        if contents == "":
            list = []
        else:
            list = eval(contents)
        
        print("\n           *************Inventory*************")
        print("\n           {:<5} {:<10} {:<10} {:<10}".format("id", "name", "price", "quantity"))
        print("           "+"=" * 40)
        for row in list:
            print("           {:<5} {:<10} {:<10} {:<10}".format(row["id"], row["name"], row["price"], row["quantity"]))




def viewOrders():
    with open("../data/orders.txt", "r") as filer:
        contents = filer.read()
        if contents == "":
            list = []
            print("\n           No orders to show!!")
            return 
        
        else:
            list = eval(contents)
        
        print("\n           ********************************************Orders********************************************")
        print("\n           {:<40} {:<10} {:<10} {:<10} {:<13} {:<10}".format("order_id", "name", "snack_id", "quantity", "total cost", "status"))
        print("           "+"=" * 93)
        for row in list:
            print("           {:<40} {:<10} {:<10} {:<10} {:<13} {:<10}".format(row["order_id"], row["name"], row["snack_id"], row["quantity"], row["total_cost"], row["status"]))






def changeOrderStatus(id):
    with open("../data/orders.txt", "r") as filer:
        contents = filer.read()
        if contents == "":
            list = []
            print("\n           No orders exist!!")
            return 
        
        else:
            list = eval(contents)
            order = [x for x in list if x["order_id"] == id] or []

            

            if (len(order)):
                origional_order = order[0]
                while True:
                    try:
                        new_status = int(input("""\n            choose the status of order from below
            1. pending
            2. dispatched
            3. delivered
                                               
            """))
                        
                        if new_status == 1:
                            order[0]['status'] = "pending"
                            break

                        elif new_status == 2:
                            order[0]['status'] = "dispatched"
                            break

                        elif new_status == 3:
                            order[0]['status'] = "delivered"
                            break

                        else:
                            print("\n            Invalid option, Please select the option from above!!")
                            continue
                        
                        
                    except ValueError:
                        print("\n            Please enter a number!!")
                        continue
                    

                

                    

                
                updated_order = order[0]



                with open("../data/orders.txt", "w") as filew:
                    updated_list_orders = [x if x != origional_order else updated_order for x in list]
                    filew.write(str(updated_list_orders))
                    if new_status == 1:
                            print("\n            Order status has been changed to pending")
                            

                    elif new_status == 2:
                        
                        print("\n            Order status has been changed to dispatched")

                    elif new_status == 3:
                        
                        print("\n            Order status has been changed to delivered")
                            
                    
                    return True


# id, name, price, avail

def mainFun():
    while True:
        try:

            choice = int(input("""\n\n           ********** Welcome to Mumbai Munchies **********
                
                Please choose from the options below
                1. Add snack to inventory
                2. Remove snack from inventory
                3. Change availabililty of snack (yes/no)
                4. Order snack
                5. View inventory
                6. View orders
                7. Change order status              
                8. Exit
                
                """))
            

            if choice == 8:
                print("\n           Thank you for the visit. Have a good day 😊")
                print("\n           ********************************************\n")
                break
            
            elif choice == 1:
                id = (input("            Enter snack id (number): "))
                name = input("            Enter snack name: ")

                while True:

                    try:
                        price = int(input("            Enter snack price: "))
                        break
                    except ValueError: 
                        print("\n            Please enter a number for price\n")
                        continue

                while True:
                    avail = input("            Enter snack availability (yes/no): ").lower()
                    if avail != "yes" and avail != "no":
                        print("\n            Please enter either 'yes' or 'no', no other values are accepted")
                    else:
                        break

                while True:

                    try:
                        quantity = int(input("            Enter snack quantity: "))
                        break
                    except ValueError: 
                        print("\n            Please enter a number for quantity\n")
                        continue


                snack = {
                    "id": id, 
                    "name": name, 
                    "price": price, 
                    "avail": avail,
                    "quantity": quantity
                    }
                addSnack(snack)

            elif choice == 2:
                flag = False
                while True:
                    remove_id = input("\n            Enter id to remove snack or enter 'back' to go back to menu: ")

                    if remove_id != "back":

                        value = removeSnack(remove_id)

                        if value:
                            break
                        else:
                            flag = True
                            break
                            
                    
                    else:
                        flag = True
                        break

                if flag:
                    continue

            
            elif choice == 3:
                id = input("\n            Enter id to change the availability of snack: ")
                changeStatus(id)

            
            elif choice == 4:
                
                while True:
                    name = input("\n            Enter your name: ")
                    id = input("\n            Enter id of the snack: ")

                    while True:

                        try:
                            quantity = int(input("\n            Enter quanity: "))
                            break
                        except ValueError:
                            print("\n            Please enter a number(interger, ie.1,2,3..) for quantity!!")
                            continue
                    
                    order_id = str(uuid.uuid4())

                    order = {
                        "order_id": order_id,
                        "name": name,
                        "snack_id": id,
                        "quantity": quantity,
                        "status": "pending"
                    }


                    flag = placeOrder(order)

                    if flag:
                        break
                    else:
                        continue
                    
            

            elif choice == 5:
                viewInventory()

            
            elif choice == 6:
                viewOrders()


            elif choice == 7:
                order_id = input("\n            Enter order id: ")
                changeOrderStatus(order_id)


            else:
                
                print("\n            Invalid option, choose the valid option!!")  

        except ValueError:
                
                print("\n            Invalid option, choose the valid option!!")  

                


            



mainFun()