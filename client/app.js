console.log("testing")

fetch('http://localhost:8000/api/')
    .then((res) => res.json())
    .then((data) => {
        const ulElm = document.getElementById('list')
        const html= data.results.map(item => <li>${item.task}</li>)
        ulElm.innerHTML = html.join('')
        console.log(data)
    })
