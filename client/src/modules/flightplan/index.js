import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { Typography} from '@material-ui/core'



const FlightPlan = () => {
    const classes = useStyles()
    return (
        <Typography variant="h5">Flight plan section</Typography>
    )
}

export default FlightPlan



/**
 * CSS Rules
 */

const useStyles = makeStyles((theme) => ({

}))