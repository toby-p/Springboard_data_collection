import springboard_functions
import json

credentials = json.load(open("../credentials/springboard_credentials.json"))

springboard_functions.Springboard_data(useremail = credentials["email"],
                                       userpassword = credentials["password"], 
                                       new_data_filepath = "../datastore/footfall_actual_daily_data.csv",
                                       primary_camera_name = "Grosvenor Bridge Link",
                                       backup_data_filepath = "../datastore_backup/footfall_actual_daily_data.csv")