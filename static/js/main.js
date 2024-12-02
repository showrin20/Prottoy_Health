let i =0;
let text_c = document.querySelector('.dynamic-text')
let text = text_c.textContent
text_c.textContent=""


const typing= ()=>{
    if (i<text.length){
        document.querySelector(".dynamic-text").innerHTML+= text[i];
        i++;
        setTimeout(typing,100)
    }
}
typing()

window.addEventListener("scroll",()=>{
    const nav = document.querySelector('nav')
    nav.classList.toggle('nav-anime',window.scrollY>10);
})
