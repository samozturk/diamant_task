import requests

response = requests.get('http://localhost:8000/')
print(response.content)

myobj = {
  "f_iban_history_available": 0,
  "f_iban_history_match": 0,
  "f_customer_iban_available": 0,
  "f_pair_ibans_matches": 0,
  "f_pair_amounts_equals": 0,
  "f_pair_invoiceId_in_reftext_leven": 0,
  "f_pair_ex_invoiceId_in_reftext_leven": 0,
  "f_reftext_op_bez_fuzzy_wuzzy": 0,
  "f_bsi_name_op_bez_fuzzy_wuzzy": 0,
  "f_customer_group_amount_match": 0
}

post_response = requests.post('http://localhost:8000/predict', json=myobj)
print(post_response.text)