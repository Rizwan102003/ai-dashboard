"use client"

import { useState } from "react"
import axios from "axios"
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts"

export default function Home() {

const [prompt,setPrompt] = useState("")
const [data,setData] = useState([])

const submitPrompt = async () => {

const res = await axios.post(
"http://127.0.0.1:8000/query",
{ prompt }
)

setData(res.data.data)

}

return (

<div style={{padding:40}}>

<h1>AI Dashboard</h1>

<input
value={prompt}
onChange={(e)=>setPrompt(e.target.value)}
placeholder="Ask a question"
/>

<button onClick={submitPrompt}>
Generate
</button>

<BarChart width={600} height={300} data={data}>
<XAxis dataKey="region"/>
<YAxis/>
<Tooltip/>
<Bar dataKey="revenue"/>
</BarChart>

</div>

)
}