import scalper

def test_main(capsys):
    # pass
    scalper.main()
    out, err = capsys.readouterr()
    assert out == 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434'
    assert err == ''


