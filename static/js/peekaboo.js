console.log('peekaboo')

document.querySelector('.start-deck').addEventListener('click',() => {
    const display = document.getElementById('1');
    // console.log(display)
    display.classList.replace("display-none", "active")
    const button = document.getElementById('start-deck-button');
        if (button.innerText =='Start Deck') { 
            button.innerText = 'Next Card'
        } 
})


