# SPC_tasks

## [boredapi](https://www.boredapi.com/api/activity )

მოცემულია ღია API, რომელიც ყოველ ჯერზე განსხვავებულ მონაცემს აგენერირებს, მაგალითად:
```JSON
{
 "activity": "Explore the nightlife of your city",
"type": "social",
"participants": 1,
"price": 0.1,
"link": "",
"key": "2237769",
"accessibility": 0.32
}
```
## დავალება მდგომარეობს შემდგომში:
დამოქეთ (mock) ენდფოინთი პოსტმენის საშუალებით, ისე, რომ რესფონსში 20 ერთეული აქტივობა (activity) იყოს, 
შემდგომ გაგზავნეთ რექვესთი თქვენს მიერ შექმნილ მოქზე და დაიმახსოვრეთ მხოლოდ ის რესფონსები სადაც ფასი მეტია ნულზე (Price > 0).
მიღებული შედეგები კი, დაალაგეთ ზრდადობის მიხედვით accessibility-პარამეტრის მიხედვით. 
