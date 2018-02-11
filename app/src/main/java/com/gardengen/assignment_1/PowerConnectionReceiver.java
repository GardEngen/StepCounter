package com.gardengen.assignment_1;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

import com.gardengen.assignment_1.interfaces.OnReceiverEvent;

import org.greenrobot.eventbus.EventBus;

///**
// * Created by Gard on 25.01.2018.
// */
//
public class PowerConnectionReceiver extends BroadcastReceiver {


//
//    MainActivity activity;
//
//    public PowerConnectionReceiver() {
//    }
//
//    public PowerConnectionReceiver(OnPowerConnected onPowerConnected) {
//        //database reference pointing to root of database
//       // Write a message to the database
//        this.onPowerConnected = onPowerConnected;
//
//        FirebaseDatabase database = FirebaseDatabase.getInstance();
//        myRef = database.getReference("steps");
//        activity = new MainActivity();
//    }
//
    @Override
    public void onReceive(Context context, Intent intent) {

        if(intent.getAction() == Intent.ACTION_POWER_CONNECTED) {
            System.out.println("jeg er koblet till");
            EventBus.getDefault().post(new OnReceiverEvent());
        } else if(intent.getAction() == Intent.ACTION_POWER_DISCONNECTED){

        }
    }
}
