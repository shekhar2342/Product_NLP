from helper.libraries import *
from helper.functions import load_model


def show_predict_page():
    st.title("Prediction")

    st.write("""### We need some information""")

    ProductName = st.text_area('Procuct Name')
    Description = st.text_area('Description')

    ok = st.button("Predict")

    if ok:

        dict_ = {
            "ProductName": [ProductName],
            "Description": [Description]
        }

        results = pd.DataFrame(dict_)

        data = load_model()
        model = data["rfc"]

        model.predict(results)

        st.subheader(model.predict(results)[0])