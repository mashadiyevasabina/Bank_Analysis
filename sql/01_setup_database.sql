IF DB_ID('BankAnalyticsDB') IS NULL
    CREATE DATABASE BankAnalyticsDB;
GO

USE BankAnalyticsDB;
GO

IF SCHEMA_ID('bronze') IS NULL
    EXEC('CREATE SCHEMA bronze');
GO

IF SCHEMA_ID('silver') IS NULL
    EXEC('CREATE SCHEMA silver');
GO

IF SCHEMA_ID('gold') IS NULL
    EXEC('CREATE SCHEMA gold');
GO