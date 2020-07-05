## Regular sequential story
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- slot{"cuisine": "Mexican"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two 300 to 700"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye

## User greeted and then only denying
* greet
    - utter_greet
* deny
    - utter_default
* deny
    - utter_default
* deny
    - utter_goodbye

## Provided location first time is not tier-1 and tier-2 city
* greet
    - utter_greet
* deny
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
	- slot{"location": "rishikesh"}
    - action_validate_location
	- slot{"location": null}
    - utter_ask_location    
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
    - action_validate_location
	- slot{"location": "mumbai"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
	- slot{"cuisine": "Chinese"}
    - action_validate_cuisine
	- slot{"cuisine": "Chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two between 300 to 700"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz.gmail.com"}
	- slot{"email": "xyz.gmail.com"}
	- action_validate_email
	- slot{"email": null}
	- utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye

## User provided cuisine name not part of Bot provided services
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
	- slot{"location": "hyderabad"}
	- action_validate_location
	- slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Spanish"}
	- slot{"cuisine": "Spanish"}
	- action_validate_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two > 300"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
    - action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
 
## first time provided budget could not be extracted or understand
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- slot{"cuisine": "South Indian"}
    - action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* out_of_scope
	- utter_default
	- utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two > 700"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@gmail.com"}
	- slot{"email": "xyz@gmail.com"}
 	- action_validate_email
	- slot{"email": "xyz@gmail.com"}
	- action_send_email
	- slot{"email": "xyz@gmail.com"}
	- utter_goodbye
 
## User does not want the email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
	- slot{"location": "bangalore"}
	- action_validate_location
	- slot{"location": "bangalore"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- slot{"cuisine": "American"}
    - action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_for_emailing
* deny
    - utter_goodbye

## User provided location and email could not be extracted or none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
	- slot{"location": "rishikesh"}
    - action_validate_location
	- slot{"location": null}
	- utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
    - action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- slot{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two between 300 to 700"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "@test.com"}
	- slot{"email": "@test.com"}
	- action_validate_email
	- slot{"email": null}
	- utter_ask_email_id
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye

## User is not providing location correctly multiple times 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": null}
	- slot{"location": null}
	- action_validate_location
	- slot{"location": null}
	- utter_ask_location
* restaurant_search{"location": null}
	- slot{"location": null}
	- action_validate_location
	- slot{"location": null}
	- utter_goodbye
	
## User providing location but not providing cuisine or it could not be extracted or is none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "marathi"}
	- slot{"cuisine": "marathi"}
	- action_validate_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "marathi"}
	- slot{"cuisine": "marathi"}
	- action_validate_cuisine
	- slot{"cuisine": null}
    - utter_goodbye

## providing location,cuisine but budget could not be extracted or none
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_validate_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- slot{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* out_of_scope
	- utter_default
	- utter_ask_budget
* out_of_scope
	- utter_default
	- utter_ask_budget
* out_of_scope
    - utter_goodbye

## provided location and cuisine during location response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi","cuisine": "mexican"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "mexican"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two Rs. 300 to 700"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@yahoo.com"}
	- slot{"email": "xyz@yahoo.com"}
    - action_validate_email
	- slot{"email": "xyz@yahoo.com"}
	- action_send_email
	- slot{"email": "xyz@yahoo.com"}
	- utter_goodbye
  
## User provided location and budget during location response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi","budget": "More than 700"}
	- slot{"location": "delhi"}
	- slot{"budget": "More than 700"}
	- action_validate_location
	- slot{"location": "delhi"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- action_validate_cuisine
	- slot{"cuisine": "chinese"}
	- utter_top_restaurant
	- action_search_restaurants
	- slot{"budget": "average cost for two More than 700"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@hotmail.com"}
	- slot{"email": "xyz@hotmail.com"}
    - action_validate_email
	- slot{"email": "xyz@hotmail.com"}
	- action_send_email
	- slot{"email": "xyz@hotmail.com"}
	- utter_goodbye

## User provided location and cuisine and budget during location response
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi","budget": "Lesser than Rs. 300","cuisine": "North Indian"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "Lesser than Rs. 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_top_restaurant
	- action_search_restaurants
	- slot{"budget": "average cost for two Lesser than Rs. 300"}
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xy_z@test.com"}
	- slot{"email": "xy_z@test.com"}
	- action_validate_email
	- slot{"email": "xy_z@test.com"}
	- action_send_email
	- slot{"email": "xy_z@test.com"}
	- utter_goodbye
  
## provided location and cuisine and budget during location response but location is not correct
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh","budget": "Rs. 300 to 700","cuisine": "North Indian"}
	- slot{"location": "rishikesh"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "Rs. 300 to 700"}
	- action_validate_location
	- slot{"location": null}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
	- slot{"budget": "average cost for two Rs. 300 to 700"}
	- utter_ask_for_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
  
## Responded location with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two Lesser than Rs. 300"}
	- utter_ask_for_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
   
## Responded cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_for_emailing
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_send_email
	- utter_goodbye
 
## Responded budget with greeting
* greet
    - utter_greet
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- action_validate_location
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_send_email
	- utter_goodbye
  
## Responded location and budget with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi","budget": "More than 700"}
	- action_validate_location
    - slot{"budget": "More than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* send_email{"email": "xyz@test.com"}
	- action_validate_email
	- action_send_email
	- utter_goodbye
   
## provided location, cuisine and budget in sequence and later email.
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_validate_email
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_goodbye

## provided location did not match with list of locations bot serves into.
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_validate_location
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - utter_ask_for_emailing
* send_email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_validate_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - utter_goodbye

## provided location cuisne and budget one by one and send an email
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "low"}
    - utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_validate_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - utter_goodbye

## provided location and cusine in one sentence and no email needed.
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "low"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye
    
## User responded location and cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian"}
	- action_validate_location
	- action_validate_cuisine
	- utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* send_email{"email": "xyz123@yahoo.com"}
	- slot{"email": "xyz123@yahoo.com"}
	- action_validate_email
	- slot{"email": "xyz123@yahoo.com"}
	- action_send_email
	- slot{"email": "xyz123@yahoo.com"}
	- utter_goodbye
	
## User responded budget and cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian","budget": "more than 300"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
	- utter_top_restaurant
	- action_search_restaurants
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_for_emailing
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_validate_email
	- slot{"email": "xyz@test.com"}
	- action_send_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
	
## User responded location and budget and cuisine with greeting
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian","budget": "more than 300"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_for_emailing
* send_email{"email": "xyz_123@outlook.com"}
	- slot{"email": "xyz_123@outlook.com"}
	- action_validate_email
	- slot{"email": "xyz_123@outlook.com"}
	- action_send_email
	- slot{"email": "xyz_123@outlook.com"}
	- utter_goodbye
	
## User responded location and budget and cuisine with greeting but said no to email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian","budget": "more than 300"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- slot{"budget": "more than 300"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
	- slot{"budget": "average cost for two more than 300"}
	- utter_ask_for_emailing
* deny
	- utter_goodbye
	
## User responded location and cuisine with greeting but said no to email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "North Indian"}
	- slot{"location": "delhi"}
	- slot{"cuisine": "North Indian"}
	- action_validate_location
	- slot{"location": "delhi"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 300"}
    - slot{"budget": "more than 300"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
    - slot{"budget": "average cost for two more than 300"}
	- utter_ask_for_emailing
* deny
	- utter_goodbye
	
## no proper response
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
	- utter_goodbye
	
## provided all details first time itself
* restaurant_search{"location": "agra", "cuisine": "American", "budget": "300 - 700 range", "email": "xyz123@yahoo.com"}
    - action_validate_location
	- slot{"location": "agra"}
    - action_validate_cuisine
	- slot{"cuisine": "american"}
	- slot{"budget": "300 - 700 range"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_search_restaurants
	- action_validate_email
	- slot{"email": "xyz123@yahoo.com"}
	- action_send_email
	- utter_goodbye
 
## provided details first time with email later
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "budget": "more than 700"}
    - action_validate_location
	- slot{"location": "Kolkata"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "abc_de_fghk@microsoft.com"}
	- action_validate_email
	- action_send_email
	- utter_goodbye
	- action_validate_email
	- slot{"email": "abc_de_fghk@microsoft.com"}
	- action_send_email
	- utter_goodbye
 
	
## without email - budget last
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   
	
## without email - cuisine last
* restaurant_search{"location": "New Delhi", "budget": "less than 300"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
 
## without email - location last
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
 
	
## without email - budget last
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye


## details first  then with email later
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "budget": "more than 700"}
    - action_validate_location
	- slot{"location": "Kolkata"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "helloworld123@infosys.com"}
	- action_validate_email
	- slot{"email": "helloworld123@infosys.com"}
	- action_send_email
	- utter_goodbye
   

	
## without email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye

	
## without email - cuisine last
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi", "budget": "less than 300"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   
	
## without email - location last
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   
	
##  without email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   

## without email - location -> cuisine ->budget
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye

	
## without email -  cuisine ->location ->budget
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   

## without email -  budget->cuisine ->location
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
  

## without email -  budget ->location->cuisine
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   
	
## without email - city  ->budget-> cuisine
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
   
	
## without email -  cuisine ->budget ->city
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
  

## without email - city -> cuisine ->budget
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye

	
## without email -  cuisine ->city ->budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
  

## without email -  budget->cuisine ->city
* greet
    - utter_greet
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye


## without email -  budget ->city->cuisine
* greet
    - utter_greet
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
 
	
## without email - city  ->budget-> cuisine
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
  
	
## without email -  cuisine ->budget ->city
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* deny
	- utter_goodbye
    
	
## with email - budget last
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.edu"}
	- action_validate_email
	- slot{"email": "xyz@test.edu"}
	- action_send_email
	- utter_goodbye

	
## with email - cuisine last
* restaurant_search{"location": "New Delhi", "budget": "less than 700"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "test11@google.co.in"}
	- action_validate_email
	- slot{"email": "test11@google.co.in"}
	- action_send_email
	- utter_goodbye

	
## with email - city last
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "test11_hello@gomail.au.com"}
	- action_validate_email
	- slot{"email": "test11_hello@gomail.au.com"}
	- action_send_email
	- utter_goodbye

## with email - budget last
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "test11.vinay@xyz.com"}
	- action_validate_email
	- slot{"email": "test11.vinay@xyz.com"}
	- action_send_email
	- utter_goodbye
 

## details provided first then email later
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "budget": "more than 700"}
    - action_validate_location
	- slot{"location": "Kolkata"}
    - action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "test11_786@gmail.com"}
	- action_validate_email
	- slot{"email": "test11_786@gmail.com"}
	- action_send_email
	- utter_goodbye
  

	
## with email - budget last
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Italian"}
    - action_validate_location
	- slot{"location": "Mumbai"}
    - action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test11.gov"}
	- action_validate_email
	- slot{"email": "xyz@test11.gov"}
	- action_send_email
	- utter_goodbye

	
## with email - cuisine last
* greet
    - utter_greet
* restaurant_search{"location": "New Delhi", "budget": "less than 700"}
    - action_validate_location
	- slot{"location": "New Delhi"}
	- slot{"budget": "less than 700"}
	- action_validate_budget
	- slot{"budget": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "test11@google.co.in"}
	- action_validate_email
	- slot{"email": "test11@google.co.in"}
	- action_send_email
	- utter_goodbye

	
## with email - city last
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "budget": "more than 700"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - action_validate_location
	- slot{"location": "Bhopal"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "hello_world@firstdata.com"}
	- action_validate_email
	- slot{"email": "hello_world@firstdata.com"}
	- action_send_email
	- utter_goodbye

	
## with email - budget las
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "test11_007@hotmail.com"}
	- action_validate_email
	- slot{"email": "test11_007@hotmail.com"}
	- action_send_email
	- utter_goodbye
  

## with email - city -> cuisine ->budget
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@sth.edu"}
	- action_validate_email
	- action_send_email
	- utter_goodbye
 
	
## with email -  cuisine ->city ->budget
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@sth.edu"}
	- action_validate_email
	- slot{"email": "xyz@sth.edu"}
	- action_send_email
	- utter_goodbye
 

## with email -  budget->cuisine ->city
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.org"}
	- action_validate_email
	- slot{"email": "xyz@test.org"}
	- action_send_email
	- utter_goodbye
 
	
## with email -  budget ->city->cuisine
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "ahbcdj@dkj.com"}
	- action_validate_email
	- slot{"email": "ahbcdj@dkj.com"}
	- action_send_email
	- utter_goodbye

	
## with email - city  ->budget-> cuisine
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "hello11world@cognizant.com"}
	- action_validate_email
	- slot{"email": "hello11world@cognizant.com"}
	- action_send_email
	- utter_goodbye
 
	
## with email -  cuisine ->budget ->city
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz123@yahoo.com"}
	- action_validate_email
	- slot{"email": "xyz123@yahoo.com"}
	- action_send_email
	- utter_goodbye
   


## with email - city -> cuisine ->budget
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "abcd@hotmail.com"}
	- action_validate_email
	- slot{"email": "abcd@hotmail.com"}
	- action_send_email
	- utter_goodbye
   
	
## with email -  cuisine ->city ->budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - action_validate_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "abcd123@googlemail.com"}
	- action_validate_email
	- slot{"email": "abcd123@googlemail.com"}
	- action_send_email
	- utter_goodbye
  

## with email -  budget->cuisine ->city
* greet
    - utter_greet
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- action_validate_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_location
* restaurant_search{"location": "Chennai"}
    - action_validate_location
	- slot{"location": "Chennai"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "xyz@test.in.au"}
	- action_validate_email
	- slot{"email": "xyz@test.in.au"}
	- action_send_email
	- utter_goodbye
    

## with email -  budget ->city->cuisine
* greet
    - utter_greet
* restaurant_search{"budget": "less than 300"}
	- slot{"budget": "less than 300"}
	- action_validate_budget
	- slot{"budget": "low"}
	- utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - action_validate_location
	- slot{"location": "Nagpur"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
	- action_validate_cuisine
	- slot{"cuisine": "American"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "abcd@outlook.com"}
	- action_validate_email
	- slot{"email": "abcd@outlook.com"}
	- action_send_email
	- utter_goodbye

	
## with email - city  ->budget-> cuisine
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - action_validate_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- action_validate_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "abc_def@yahoo.com"}
	- action_validate_email
	- slot{"email": "abc_def@yahoo.com"}
	- action_send_email
	- utter_goodbye
   
## with email -  cuisine ->budget ->city
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
	- action_validate_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "more than 700"}
	- slot{"budget": "more than 700"}
	- action_validate_budget
	- slot{"budget": "high"}
	- utter_ask_location	
* restaurant_search{"location": "Pune"}
    - action_validate_location
	- slot{"location": "Pune"}
	- utter_top_restaurant
	- action_search_restaurants
	- utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "hello-world@fiserv.com"}
	- action_validate_email
	- slot{"email": "hello-world@fiserv.com"}
	- action_send_email
	- utter_goodbye

  
## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* send_email{"email": "abc_12345@yahoo.com"}
    - slot{"email": "abc_12345@yahoo.com"}
    - action_validate_email
    - slot{"email": "abc_12345@yahoo.com"}
    - action_send_email
    - slot{"email": "abc_12345@yahoo.com"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Mumbai", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "banaglore", "budget": " 300 to 500"}
    - slot{"budget": " 300 to 500"}
    - slot{"location": "banaglore"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "marathi"}
    - slot{"cuisine": "marathi"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* send_email{"email": "abc123@gmail.co.in"}
    - slot{"email": "abc123@gmail.co.in"}
    - action_validate_email
    - slot{"email": "abc123@gmail.co.in"}
    - action_send_email
    - slot{"email": "abc123@gmail.co.in"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "sounth indian", "location": "chennai", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "sounth indian"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye

## interactive_story_1
* restaurant_search{"budget": "high", "cuisine": "north indian", "location": "chennai", "email": "singhvinay@yahoo.co.in"}
    - slot{"budget": "high"}
    - slot{"cuisine": "north indian"}
    - slot{"email": "singhvinay@yahoo.co.in"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - action_validate_email
    - slot{"email": "singhvinay@yahoo.co.in"}
    - action_send_email
    - slot{"email": "singhvinay@yahoo.co.in"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"budget": "mid", "location": "bangalore", "cuisine": "american"}
    - slot{"budget": "mid"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "location": "Kanpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Kanpur"}
    - action_validate_location
    - slot{"location": "Kanpur"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexicano", "location": "Mumbai"}
    - slot{"cuisine": "mexicano"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "abc_def.786@gmail.com"}
    - slot{"email": "abc_def.786@gmail.com"}
    - action_validate_email
    - slot{"email": "abc_def.786@gmail.com"}
    - action_send_email
    - slot{"email": "abc_def.786@gmail.com"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_validate_location
    - slot{"location": "Hyderabad"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - utter_ask_for_emailing
* send_email{"email": "singhvnay@gmail.com"}
    - slot{"email": "singhvnay@gmail.com"}
    - action_validate_email
    - slot{"email": "singhvnay@gmail.com"}
    - action_send_email
    - slot{"email": "singhvnay@gmail.com"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_validate_location
    - slot{"location": "indore"}
    - utter_ask_cuisine
* restaurant_search
    - action_validate_cuisine
    - slot{"cuisine": "thai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "high"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye
* goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gaon"}
    - slot{"location": "gaon"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_validate_location
    - slot{"location": "raipur"}
    - utter_ask_cuisine
* restaurant_search
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* affirm
    - utter_ask_email_id
* send_email{"email": "ankitapaithankar16@gmail.com"}
    - slot{"email": "ankitapaithankar16@gmail.com"}
    - action_validate_email
    - slot{"email": "ankitapaithankar16@gmail.com"}
    - action_send_email
    - slot{"email": "ankitapaithankar16@gmail.com"}
    - utter_goodbye

## interactive_story_1
* out_of_scope
    - utter_default

## interactive_story_1
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
    - utter_goodbye

## interactive_story_1
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default
    - utter_goodbye
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "low"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "low"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_search_restaurants
    - slot{"budget": "mid"}
    - utter_ask_for_emailing
* deny
    - utter_goodbye
