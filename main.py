from predict import train

def main():
    train()
    
    from dashboard import app
    app.run_server(debug=True)

if __name__=='__main__':
    main()