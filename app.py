from PIL import Image
import streamlit as st

with st.container():
    img = Image.open('C:/Users/Admin/OneDrive/Documents/Python Scripts/project/Burger_venv/Image/shop.png')
    st.title("Welcome You to Burger World")
    st.image(img, width = 700)

st.write("---")

#price of burgers
with st.container():
    st.subheader("Price List of Burger")
    st.write("Veg Patty Burger without cheese = 150")
    st.write("Chicken Patty Burger without cheese = 200")
    st.write("Beef Patty Burger without cheese = 250")
    st.write("Veg Patty Burger with cheese = 200")
    st.write("Chicken Patty Burger with cheese = 250")
    st.write("Beef Patty Burger with cheese = 300")
     

st.write("---")

# Your selection
buns = st.selectbox("Select Bun", ["None", "Plain Bun", "Sesame Seed Bun", "Whole Wheat Bun"])
patties = st.selectbox("Select Patty", ["None", "Beef Patty", "Chicken Patty", "Veggie Patty"])
cheese = st.radio("Do you want cheese", ("None", "Yes", "No"))
layer = st.slider("How Many layers of cheese do you want?", 1, 5,)
veggies = st.multiselect("Select Vegetables", ["Lettuce", "Tomato", "Onion", "Pickles"])
sauces = st.multiselect("Select Sauces", ["Ketchup", "Mustard", "Mayonnaise"])


#quantity of burger do you want
quantity = st.number_input("Enter the Quantity of burger:", value = 0)

     
#click for confirm your types burger
st.button("Click Me")
if(st.button("Ok")):  
    if buns == "None":
        st.write("Please select type of bun") 
    elif patties == "None":
        st.write("Please select type of Patties")  
    elif  cheese == "None":
        st.write("Please select yes or no")     
    elif quantity == 0:
        st.write("Please select a quantity")       
    else:
        st.write("Your Selections")
        st.write("---")


# Burger composition
        with st.container():
            st.subheader("Your Burger Type:")
        st.write(" Bun:",buns)
        st.write(" Patty:", patties)
        st.write(" Cheese:",cheese)
        st.text(" Layers of cheese you selected:{}".format(layer) )
        st.write(" Vegetables: " + ", ".join(veggies))
        st.write(" Sauces: " + ",".join(sauces))
        st.write(" Quantity:", quantity)


    #price list of different types of burgers
        with st.container():
            Veg_patty_burger_without_cheese  = 150
            Chicken_patty_burger_without_cheese = 200
            Beef_patty_burger_without_cheese = 250
            Veg_burger_with_cheese  = 200
            Chicken_patty_burger_with_cheese = 250
            Beef_patty_burger_with_cheese = 300
            
            #veg patty burger without cheese
            if patties == "Veggie Patty" and cheese == "No":
                total = (Veg_patty_burger_without_cheese) * quantity
                st.write("---")
                st.write("Total Price = ",total)
                st.write("---")
            #chicken patty burger without cheese    
            elif patties == "Chicken Patty" and cheese == "No":
                total = (Chicken_patty_burger_without_cheese) * quantity 
                st.write("---")
                st.write("Total Price = ",total) 
                st.write("---")
            #beef patty burger without cheese    
            elif patties == "Beef Patty" and cheese == "No":
                total = (Beef_patty_burger_without_cheese) * quantity
                st.write("---")
                st.write("Total Price = ",total) 
                st.write("---")
            #veg patty with cheese    
            elif patties == "Veggie Patty" and cheese == "Yes":
                total = (Veg_burger_with_cheese) * quantity
                st.write("---")
                st.write("Total Price = ",total)
                st.write("---")
            #chicken patty with cheese    
            elif patties == "Chicken Patty" and cheese == "Yes":
                total = (Chicken_patty_burger_with_cheese) * quantity 
                st.write("---")
                st.write("Total Price = ",total) 
                st.write("---")
            #beef patty with cheese    
            elif patties == "Beef Patty" and cheese == "Yes":
                total = (Beef_patty_burger_with_cheese) * quantity 
                st.write("---")
                st.write("Total Price = ",total) 
                st.write("---")
            else:
             st.write(" ")  


    #If you want cheese display cheese burger or without cheese display without cheese burger
        with st.container():
            if cheese == "Yes":
                img1 = Image.open('C:/Users/Admin/OneDrive/Documents/Python Scripts/project/Burger_venv/Image/burger.png')
                st.image(img1, width=500)
            else:
                img2 =  Image.open('C:/Users/Admin/OneDrive/Documents /Python Scripts/project/Burger_venv/Image/no cheese.png')    
                st.image(img2, width = 400)
    
            #quantity of burgers ready 
            st.subheader("Your {} Burger was Ready".format(quantity))
