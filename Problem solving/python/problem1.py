#ধর একটা অ্যারে বা লিস্ট আছে যেমনঃ
#const nameList =["Torikus sadik", "Arafat Hossain", " Shakil Haque", "Fahim Morshed"," Shakil Babu"]
#এই লিস্ট বা এ্যারের মধ্যে সবচেয়ে ছোট নাম কোনটা তা প্রিন্ট করে দেখাও?

listu = ['torikus sadik','Shakil babu','Shakil haque','Arafat hossain','Fahim morshed']
listu.sort(key=len)
piccu = listu[0]
print(piccu)