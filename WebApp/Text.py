import html
shif_enter = html.unescape("<br />")

fuel_type_list = ["Regular gasoline", "Premium gasoline", "Diesel", "Ethanol (E85)",
                  "Natural Gas"]

transmission_type_list = ["M", "A", "AM", "AS", "AV"]
# transmission_type_list = ["Manual (M)", "Automatic (A)", "Automated Manual (AM)",
                            # "Automatic With Select Shift (AS)", "Continuously Variable (AV)"]

vehicle_class_list = ["Minicompact", "Subcompact", "Compact", "Mid-size", "Full-size",
                      "Station wagon", "Pickup truck", "Minivan", "Van", "Sport utility vehicle",
                      "Two-seater", "Special purpose vehicle"]
# vehicle_class_list = ["MiniCompact", "SubCompact", "Compact", "Mid-Size", "Full-Size",
                    #   "Station Wagon", "Pickup Truck", "MiniVan", "Van", "Sport Utility Vehicle (SUV)",
                    #   "Two-Seater", "Special Purpose Vehicle"]

manufacturer_list = ['Chevrolet', 'Ford', 'BMW', 'GMC', 'Mercedes-Benz', 'Toyota', 'Dodge',
                     'Porsche', 'Audi', 'Volkswagen', 'Nissan', 'Mazda', 'Honda', 'Hyundai', 'Jeep', 'Subaru',
                     'Volvo', 'Kia', 'Lexus', 'Cadillac', 'Chrysler', 'MINI', 'Jaguar', 'Pontiac', 'Buick',
                     'Mitsubishi', 'Acura', 'Infiniti', 'Land Rover', 'Suzuki', 'Lincoln', 'Saab', 'Saturn',
                     'Bentley', 'Ram', 'Maserati', 'Rolls-Royce', 'Lamborghini', 'Aston Martin', 'Ferrari',
                     'Plymouth', 'FIAT', 'Oldsmobile', 'Genesis', 'Alfa Romeo', 'Mercury', 'Isuzu', 'Scion',
                     'Eagle', 'Daewoo', 'smart', 'Hummer', 'Geo', 'Bugatti',]


fuel_model_url = "https://github.com/Alireza-Esp/VFCPM/raw/refs/heads/main/Model%20&%20Objects/model-fuel.pkl"

CO2_model_url = "https://github.com/Alireza-Esp/VFCPM/raw/refs/heads/main/Model%20&%20Objects/model-CO2.pkl"

encoder_url = "https://github.com/Alireza-Esp/VFCPM/raw/refs/heads/main/Model%20&%20Objects/encoder.pkl"

standardizer_url = "https://github.com/Alireza-Esp/VFCPM/raw/refs/heads/main/Model%20&%20Objects/standardizer.pkl"

welcome_text = """
Whats the meaninig of VFCP? VFCP stands for "Vehicle Fuel Consumption Predictor".\
this is a Machine Learning Model that predict the rate of fuel consumption and \
CO2 emission of a vehcile with respect to it's some characteristics like "Engine Size", \
"Number of Cylinders", "Fuel Type" and ... . Detialed informations of the project \
are explained in references. Are you excited? Let's use the model!
"""

sidebar_css = """
<style>
    [data-testid="stSidebar"]{
        min-width: 400px;
        max-width: 400px;
    }
</style>
"""

sidebar_text1 = """
🔹 This project has been defined as the "Final Undergraduate Project" and carried out  by:
"""

sidebar_text2 = """👨‍🎓 Alireza Esmaeilpour Peynavandi
👨‍🏫 Supervising Professor: Dr. Alyari
⚙️ Field of Study:\n\t   Mechanical Engineernig - Automotive Subfield
🏬 University:\n\t   Shahid Rajaee Teacher Training University
📧 Email:\n\t   Alireza.esp07@gmail.com
🌐 Website: \n\t   Alireza-Esp.ir
🔗 GitHub:\n\t   Github.com/Alireza-Esp\n\n\n
Semester 8 - Winter 1403"""

help_text = f"""Well, the VFCP is very easy to use! as previously satated, the model has \
some features; that listed below:{shif_enter}
▪️ Number Of Cylinders{shif_enter}
▪️ Engine Size{shif_enter}
▪️ Fuel Type{shif_enter}
▪️ Transmission Type{shif_enter}
▪️ Number Of Gears{shif_enter}
▪️ Vehicle Class{shif_enter}
▪️ Model Year{shif_enter}
▪️ Manufacturer{shif_enter}
In fact, this features is related to the vhicles that the model has trained from; and \
if you want to make a prediction with model, you should pass this features to the model \
and see that it predicts the "Combined Fuel Consumption" and "CO2 Emission" of your intended sample.{shif_enter}\
However, there are some considerations that you should keep in mind. For example it's \
better to enter interval [1995,2025] for "Model Year" feature however that the model \
can make a prediction even if the values be outside of the interval. Or it's good \
enter standard values for "Number Of Cylinders" featur; you know that probably we haven't \
"11 Cylinders" vehicle.
"""

prediction_text = """Enter your intended features for prediction...
"""
