# Real Estate Listing Optimization

This repository contains a Python script that sorts a list of house listings and returns the most recent listing of each address. The script takes in a list of house listings in the format `name, address, date`, and outputs a list of the most recent listing of each address.

## Problem Description

In this problem, you are given a set of house listings and your job is to return a list of the most recent listing of each address. There could be multiple listings of the same address, and you must ensure your output contains only one listing per address (the most recent one). A listing contains a name, address, and date.

### Example

#### Input:
L4, 123 kings road,2022

L1, 123 kings road,2020

L2, 20 queen road,1990

L3, 20 queen road,1992

#### Expected Output: (L4, L3)

In the above example, there are two listings with the same address "123 kings road", and two listing with the same address "20 queen road". The output includes the most recent listing with the address "123 kings road" (2022 > 2020) which is L4, and the most recent listing with the address "20 queen road" (1992 > 1990) which is L3, hence (L4, L3).


