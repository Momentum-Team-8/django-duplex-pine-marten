// Big shot-out to Amy & Jeanette for the JS!
let display = document.getElementById('1');
let counter = 1
let nextButton = document.getElementById('next-button')

document.querySelector('.start-deck').addEventListener('click',() => {
    display.classList.replace("display-none", "active")
    nextButton.classList.replace("display-none", "next-button")
})

nextButton.addEventListener('click', () => {
    counter ++
    display = document.getElementById(`${counter}`)
    display.classList.replace("display-none", "active")
    display.scrollIntoView()
})


