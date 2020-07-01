import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { Typography } from '@material-ui/core'


const FlightPlanBrowser = () => {
    const classes = useStyles()   

    return (
        <div>
            <Typography>Browser content</Typography>
        </div>        
    )
}

export default FlightPlanBrowser



/**
 * CSS Rules
 */

const useStyles = makeStyles((theme) => ({
    
}))