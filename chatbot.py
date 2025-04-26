products = {
    "laptop": {
        "name": "Laptop",
        "price": 1200,
        "description": "A high-performance laptop for work and play.",
        "category": "electronics",
        "related": ["headphones", "smartphone"]
    },
    "smartphone": {
        "name": "Smartphone",
        "price": 800,
        "description": "A sleek smartphone with a great camera and display.",
        "category": "electronics",
        "related": ["headphones"]
    },
    "headphones": {
        "name": "Headphones",
        "price": 150,
        "description": "Noise-cancelling headphones for immersive sound.",
        "category": "accessories",
        "related": ["smartphone"]
    }
}
from datetime import datetime

def greet_user():
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    print(f"{greeting}! Welcome to the ShopBot. How can I assist you today?")

def show_products(category=None):
    if category:
        print(f"Here are the products in the {category} category:")
        for product in products:
            if products[product]["category"] == category:
                print(f"- {products[product]['name']} (${products[product]['price']})")
    else:
        print("We have the following products available:")
        for product in products:
            print(f"- {products[product]['name']} (${products[product]['price']})")

def get_product_info(product_name):
    product = products.get(product_name.lower())
    if product:
        print(f"{product['name']}: {product['description']} - ${product['price']}")
        suggest_related_products(product_name)
    else:
        print("Sorry, we don't have that product.")

def suggest_related_products(product_name):
    product = products.get(product_name.lower())
    if product and product['related']:
        print("You might also be interested in:")
        for related_product in product['related']:
            related = products.get(related_product)
            print(f"- {related['name']} (${related['price']})")

def handle_order(product_names):
    total = 0
    for product_name in product_names:
        product = products.get(product_name.lower())
        if product:
            total += product['price']
            print(f"Added {product['name']} to your cart for ${product['price']}.")
        else:
            print(f"Sorry, we don't have {product_name}.")
    
    if total > 0:
        print(f"Your total order amount is ${total}.")
        print("Your order has been placed successfully.")
    else:
        print("No valid products were ordered.")

def handle_common_questions(query):
    faq = {
        "store hours": "Our store is open from 9 AM to 9 PM, Monday to Saturday.",
        "return policy": "You can return any product within 30 days of purchase with a valid receipt.",
        "shipping": "We offer free shipping on orders over $50."
    }
    
    for question, answer in faq.items():
        if question in query:
            print(answer)
            return
    
    print("I'm sorry, I didn't understand that. Can you please rephrase?")

def chatbot():
    greet_user()
    
    while True:
        user_input = input("\nYou: ").lower()

        if "show products" in user_input:
            if "electronics" in user_input:
                show_products("electronics")
            elif "accessories" in user_input:
                show_products("accessories")
            else:
                show_products()
        elif "info" in user_input:
            product_name = user_input.replace("info", "").strip()
            get_product_info(product_name)
        elif "order" in user_input:
            product_names = user_input.replace("order", "").strip().split(",")
            handle_order(product_names)
        elif any(question in user_input for question in ["store hours", "return policy", "shipping"]):
            handle_common_questions(user_input)
        elif "bye" in user_input or "exit" in user_input:
            print("Thank you for visiting! Have a great day!")
            break
        else:
            print("I'm sorry, I didn't understand that. Please type 'show products', 'info <product>', 'order <product1, product2>', or 'bye' to exit.")

if __name__ == "__main__":
    chatbot()

