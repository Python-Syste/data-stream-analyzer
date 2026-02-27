from src.data_cleaning import load_and_clean_data
from src.visualization import plot_sales
from src.train_model import train_sales_model

def main():
    df = load_and_clean_data()

    plot_sales(df)

    model = train_sales_model(df)

    print("Model trained successfully")

if __name__ == "__main__":
    main()
