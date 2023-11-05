import streamlit as st
from datetime import date
import portfolio as pf
import time
import utils as ut
from plotly import graph_objs as go
import pie
Level = [1, 2, 3, 4, 5]
currLevel = st.selectbox("Choose Level ", Level)
investment = pf.getInvest()
def display_message(message, message_container):
	    # Create the message-shaped background with text
        message_container.write('<div class="message">'+message+'</div>', unsafe_allow_html=True)
        time.sleep(3)
        message_container.empty()
#styles
style = """
	<style>
	.message {
		background-color: #f5f5f5; /* Off-white background color */
		padding: 10px;
		border: 2px solid #000; /* Black border */
		border-radius: 10px;
		font-weight: bold; /* Bold text */
		color: #000; /* Black text color */
	}
	</style>
	"""
	# Apply the CSS style
st.write(style, unsafe_allow_html=True)
#
START = "2022-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

message_container = st.empty()
display_message(f"{str(currLevel*30)} mins = 1 day" , message_container)
st.title('GameStock')
col1, col2 = st.columns([1,2])
with col1:
    amount = st.empty()
    amount.text("Investment:$"+str(investment))
with col2:
     st.text("Time")
st.subheader("Portfolio")
portfolio_container = st.empty()
portfolio_container.table(pf.getPortfolio())
stocks = {"Google":'GOOG', "Apple":'AAPL', "Microsoft":'MSFT', "Amazon":'AMZN'}


col1, col2 = st.columns([1, 2])
with col1:
    selected_stock = st.selectbox('Choose stock', stocks.keys())
    #Display a message    
    message_container = st.empty()
    if currLevel >= 3:
         pie.setPie(st)

# Plot raw data
def plot_raw_data(data):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)

with col2:
    data = ut.load_data(selected_stock, stocks)
    plot_raw_data(data)
    if currLevel >= 2:
        st.subheader("Stock Metrics")
        data_table = ut.load_fast_info(selected_stock, stocks)
        st.table(data_table)
action = st.selectbox("Action", ["Buy", "Sell"])
symbol = st.text(selected_stock)
shares = st.number_input("Shares", min_value=1)

# Perform the action
if st.button("Execute"):
    if action == "Buy":
        investment -=pf.buy_stock(stocks[selected_stock], shares)
        pf.setInvest(investment)
        amount.text("Investment:$"+str(investment))
        portfolio_container.table(pf.getPortfolio())
        
    elif action == "Sell":
        investment += pf.sell_stock(stocks[selected_stock], shares)
        pf.setInvest(investment)
        amount.text("Investment:$"+str(investment))
        portfolio_container.table(pf.getPortfolio())

#Q&A
context = ""
answerbox = st.empty()
context = answerbox.text_area("Your query will be answered here:", value=context, key="context")
question = st.text_input("Enter Question:")
if st.button("Get Answer"):
    answer="Hello got to the answer"
	#answer = answer_question(context, question)
    context = answerbox.text_area("",value=answer, key="answer", disabled=True)