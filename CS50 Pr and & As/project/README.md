# Mortgage calculator

#### Video Demo:  <URL HERE>

### Description: The project I decided on was a mortgage calculator, which has three different functions that show amounts from a mortgage loan that aren't easy to see from the beginning. I made this calculator after seeing one of the mortgage bills from my mother, which completely shocked me since almost 90% of the monthly bill she was paying went to pay the interest and a small fraction actually paid off our home. So, I wanted to build a calculator that allowed users to have more information about their mortgage before rushing themselves to a decision.

#### For all three of the functions, I debated whether to put the user input in the main() function or the functions themselves. I decided on placing the input on the functions themselves, which proved to be not the best idea in the long term, but regardless, it decluttered the main function and allowed for better readability in my opinion. Due to the decision of placing the user input in the other functions, I had to learn a new concept in python and put it in practice, so maybe it wasn't that bad of a decision after all.

#### The first function of the calculator asks for input from the user in order to return the total amount of interest that will be paid at the end of the loan. Usually, the total interest paid at the end of the loan will end up being a little over the original amount of the home value. The calculator takes into account the fact that you will be paying less interest over time and more into the principal value of the home. The calculator does not take into account adjustable interest loans since that would be severely more convoluted.

#### The second function created returns a hypothetical amortization payment. Amortization is a monthly amount that is paid to the loaning institution which stays constant. Over time, a higher percentage of the amortization payment goes to pay the principal of the loan rather than the interest. The function is similar to calcInterest() because it needs three inputs from the user: their mortgage loan, interest rate, and term. The formula that helped me the most for this project came from this video: https://youtu.be/S6CN7y96LV8?si=r731MO-he7qnBAqO, which details how to calculate interest and amortization on a mortgage loan.

#### The third function created was more complicated than the other two, this is because, even though it asks for just one input from the user, I needed to rearrange the function in order to solve for a value of a home rather than an amortization payment. Although, in a sense, it could be considered simpler because I am considering and average loan term of 30-years and a fixed interest rate of 6.5%. This function helps users find a budget home on their income without needing to delve too much into the complexities of a mortgage loan.

#### Smaller functions were also created in order to aid the three main functions, these include: choice(), valueMorgage(), valueInterest(), and valueTime(). All functions have failsafes that ensure the user inputs a number which the formula can work with.

#### The test functions were, admittedly, one of the harder parts of the project. I was not familiar with any methods to test functions that asked for user input. I searched high and wide and, eventually, found a very useful article linked here: https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9, which uses monkeypatch to test the functions. It took some trial and error, but the test functions were built and work beautifully.

TODO
