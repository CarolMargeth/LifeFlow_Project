-- DATABASE SCRIPT

CREATE DATABASE LifeFlow;

-- Create User Table
CREATE TABLE Users (
    User_ID SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    middle_name VARCHAR(20),
    last_name VARCHAR(20),
    age INTEGER,
    height INTEGER,
    email VARCHAR(50)
);

-- Create Daily Metrics Table
CREATE TABLE DailyMetrics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(User_ID),
    date DATE,
    mood VARCHAR(20),
    energy VARCHAR(20),
    appetite VARCHAR(20),
    cravings VARCHAR(20),
    sleep_quality VARCHAR(20),
    sleep_time INTEGER,
    workout_time INTEGER,
    workout_type VARCHAR(20)
);

-- Create Health Metrics Table
CREATE TABLE HealthMetrics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(User_ID),
    date TIMESTAMP,
    metric_type VARCHAR(20),
    metric_value DECIMAL(3,2)
);

-- Create Annotations Table
CREATE TABLE Annotations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(User_ID),
    date DATE,
    comment CHARACTER(100)
);

-- Create Diseases Table
CREATE TABLE Diseases (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(User_ID),
    date DATE,
    diagnostic VARCHAR(50)
);

-- Create Medication Table
CREATE TABLE Medication (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(User_ID),
    date DATE,
    medicationName VARCHAR(20)
);

