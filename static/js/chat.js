
async function sendMessage(){

const input = document.getElementById("promptInput")
const msg = input.value.trim()

if(!msg) return

const chat = document.getElementById("chatBox")

const user = document.createElement("div")
user.className="user"
user.innerText=msg
chat.appendChild(user)

input.value=""

const ai = document.createElement("div")
ai.className="ai"
ai.innerText="Thinking..."
chat.appendChild(ai)

chat.scrollTop = chat.scrollHeight

const res = await fetch("/api/process/",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({prompt:msg})
})

const data = await res.json()

ai.innerText=data.response

chat.scrollTop = chat.scrollHeight
}

function newChat(){
document.getElementById("chatBox").innerHTML='<div class="ai">New chat started.</div>'
}
