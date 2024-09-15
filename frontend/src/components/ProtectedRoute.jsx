import {Navigate} from 'react-router-dom'
import {jwtDecode} from 'jwt-decode'
import api from '../api'
import { REFRESH_TOKEEN, ACCES_TOKEN } from '../constants'
import { useState, useEffect } from 'react'



function ProtectRoute({ children }){

    const [isAuthorized, setIsAuthorised] = useState(null)
    useEffect(() => {
        auth().catch(()=> setIsAuthorised(false))
    },[])

    const refreshToken = async() =>{
        const refreshToken = localStorage.getItem(REFRESH_TOKEEN)

        try {
            const res = await api.post("/api/user/refresh/",{
                refresh : refreshToken,
            });
            if (res.status === 200){
                localStorage.setItem(ACCES_TOKEN, res.data.access)
                setIsAuthorised(true)
            }
            else{
                setIsAuthorised(false)
            }
        } catch (error) {
            console.log(error)
            setIsAuthorised(false)
            
        }

    };
    
    const auth = async() =>{
        const token = localStorage.getItem(ACCES_TOKEN)

        if (!token){
            setIsAuthorised(false)
            return
        }
        const decoded = jwtDecode(token)
        const tokenExpiratipn = decoded.exp
        const now = Date.now()/1000
        if (tokenExpiratipn < now)
        {
            await refreshToken()
        }
        else
        {
            setIsAuthorised(true)
        }
    };

    if (isAuthorized === null){
        return <div>Loading ...</div>
    };

    return isAuthorized ? children : <Navigate> to="/login"</Navigate>
}

export default ProtectRoute