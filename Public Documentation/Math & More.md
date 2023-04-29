### Thursday 27.04.2023 8pm

For the technical background a thorough discussion of the employed methods is essential for transparency reasons.

Initially I set the assumption to not go overboard with too crazy models and stick to some basic workhorse-methods. Specifically I think about some econometrical models like ARIMA, maybe VARMA or VECM, which should be the upper limit. However I want to try implementing something like Prophet or XGboost. Maybe I will focus. Can't tell yet.

A good and basic start for practical implementation is a good old, regular univariate parametric regression without bells and whistles. Just some trend over time with the ability to set a rolling window.

### Linear Regression - The basics

This model 