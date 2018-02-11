package com.gardengen.assignment_1.interfaces;

/**
 * Created by Gard on 30.01.2018.
 */

public class OnReceiverEvent {
    int steps;

    public OnReceiverEvent(int steps) {
        this.steps = steps;
    }

    public OnReceiverEvent() {
    }

    public int getSteps() {
        return steps;
    }

    public void setSteps(int steps) {
        this.steps = steps;
    }
}
