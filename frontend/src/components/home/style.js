import styled from 'styled-components';

export const BackgroundColor = styled.main`
background-color: #f8f8f8;
`;

export const HeaderImageContainer = styled.div`
width: 100%;
height: 40vh;
display: flex;
align-items: center;
justify-content: center;
`;

export const HeaderImage = styled.img`
width: 100%;
height: 40vh;
object-fit: cover;
`;

export const SearchBarContainer = styled.div`
position: absolute;
width: 40vw;
`;

export const InputField = styled.input`
border: none;
padding: 20px;
width: 30vw;
background-color: white;
border-radius: 5px;
`;

export const ButtonPlaceholder = styled.button`
background-color: #e47d32;
height: 20px;
width: 100px;
margin: 20px;
border:none;
color: white;
`;

export const HeadlineContainer = styled.div`
display: flex;
justify-content: center;
`;

export const RestaurantHeadline = styled.p`
font-size: 1.5rem;
text-transform: uppercase;
text-align: center;
padding: 15px;
border-bottom: 2px solid #e47d32;
color: #4c4c4c;
`;