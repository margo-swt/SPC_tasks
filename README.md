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

### How is task completed
At first we send "GET" request to  [boredapi](https://www.boredapi.com/api/activity )
In order to view the data and save it as example for our mock server

In this example , we have created 20 activities with different values of price and accessibility

#### The next request is for our mock server
This request will return the  response of our example, with the help of our test section, we can filter the responses via required parameters

provided script helps us to filter respons with the prices above 0
we can check this response in log by
```JavaScript
console.log(filterPrice)
```

```JavaScript

    const myResponse = pm.response.json();
    let filterPrice = myResponse.filter(price => price.price > 0);
    
 ```
Next  script is used to sort the parameters with accessibility value, by ascending

```JavaScript
    let sortedByAccessibilityAsc = filterPrice.sort((a1, a2) =>
        (a1.accessibility > a2.accessibility) ? 1 :
            (a1.accessibility < a2.accessibility ? -1 : 0))

    //Here we will log the final result of our function | 
    // parameters, that have price > 0 , will be sorted with accessibility ascending 
    console.log(sortedByAccessibilityAsc)
```

#### We can also use an async function to achieve our goal

```JavaScript
pm.test("Price greater than 0 and sorted via accessibilitu asc", async function () {
    const data = await pm.response.json();
    const filteredData = data.filter(price => price.price > 0);
    filteredData.sort((a1, a2) => (a1.accessibility > a2.accessibility) ? 1 : (a1.accessibility < a2.accessibility ? -1 : 0))
    console.log(filteredData)
})

```
