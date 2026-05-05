# Chapter 12: Regression — Lab Report

## Student Information
- Name: Huy Nguyen
- Date: 05/04/2026
- Course: COSC 2436

## Algorithm Summary

In this lab, I used KNN regression to predict how many loaves a bakery should bake. The model uses weather, weekend/holiday status, and game status as features. It compares today’s conditions to similar past days and predicts a loaf amount based on nearby examples.

## Test Results

Program runs successfully:
- Bakery data loads correctly
- Features and target values are separated correctly
- KNN model trains with k=4
- Predicted loaves are generated for today’s conditions

## Reflection Questions

1. What is regression used for?  
Regression is used to predict a number based on patterns in data.

2. Why use KNN regression here?  
KNN regression works because it compares today’s conditions to similar past days.

3. What features affected the prediction?  
Weather, weekend/holiday status, and game status affected the prediction.

## Challenges Encountered

Understanding how KNN can be used for prediction was confusing at first. After seeing how the model compares today’s inputs to past data, it made more sense.
