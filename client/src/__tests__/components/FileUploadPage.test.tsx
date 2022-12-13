import {render, screen} from '@testing-library/react'
import '@testing-library/jest-dom'
import FileUploadPage from '../../components/FileUploadPage'
import FileUploadButton from '../../components/FileUploadButton'

test('Should render sagewhale logo', async () => {
    render(<FileUploadPage />)

    expect(screen.getByAltText("Sagewhale")).toBeInTheDocument()
})

test('Should render file upload button', async () => {
    render(<FileUploadButton />)

    expect(screen.getByRole('button')).toHaveTextContent('Upload File')
})
