async function sendMessage(){

const input = document.getElementById("promptInput")
const message = input.value.trim()

if(!message) return

const chatBox = document.getElementById("chatBox")

// user message
const userMsg = document.createElement("div")
userMsg.className = "user"
userMsg.innerText = message
chatBox.appendChild(userMsg)

input.value = ""

// AI loading message
const aiMsg = document.createElement("div")
aiMsg.className = "ai"
aiMsg.innerText = "Thinking..."
chatBox.appendChild(aiMsg)

chatBox.scrollTop = chatBox.scrollHeight

try{

const res = await fetch("/api/process/",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({prompt:message})
})

const data = await res.json()

aiMsg.innerText = data.response

}catch(error){

aiMsg.innerText = "Error connecting to AI"

}

chatBox.scrollTop = chatBox.scrollHeight
}
