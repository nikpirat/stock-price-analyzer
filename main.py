from src.analyzer import summary_stats, calculate_daily_return
from src.data_cleaner import clean_data
from src.data_loader import load_csv
from src.visualizer import plot_price, plot_moving_averages, plot_daily_returns_histogram


def main():
    df = load_csv('data/stock_data.csv')
    df = clean_data(df)
    df = calculate_daily_return(df)

    stats = summary_stats(df)
    print("Summary statistics: ", stats)

    plot_price(df)
    plot_moving_averages(df)
    plot_daily_returns_histogram(df)

if __name__ == '__main__':
    main()