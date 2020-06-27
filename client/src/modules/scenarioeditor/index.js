import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { Typography } from '@material-ui/core'



const ScenarioEditor = () => {
    const classes = useStyles()
    return (
        <Typography variant="h5">Scenario editor section</Typography>
    )
}

export default ScenarioEditor



/**
 * CSS Rules
 */

const useStyles = makeStyles((theme) => ({

}))