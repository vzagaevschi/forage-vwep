from pink_morsels_visualisation import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_subheader_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#subheader", timeout=10)


def test_plot_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#plot", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=10)
